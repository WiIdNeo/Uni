using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

namespace DocumentIngestion
{
    public class DocumentCleaner
    {
        public string Clean(string rawText)
        {
            Console.WriteLine("[DEBUG] DocumentCleaner: Starte Reinigung...");

            var pages = rawText.Split("--- PAGE BREAK ---", StringSplitOptions.RemoveEmptyEntries)
                               .Select(p => p.Trim())
                               .ToList();

            Console.WriteLine($"[DEBUG] DocumentCleaner: Seiten erkannt: {pages.Count}");

            // Kopf- und Fußzeilen sammeln
            var firstLines = new List<string>();
            var lastLines = new List<string>();

            foreach (var page in pages)
            {
                var lines = page.Split('\n', StringSplitOptions.RemoveEmptyEntries)
                                .Select(l => l.Trim())
                                .ToList();

                if (lines.Count == 0) continue;

                firstLines.Add(lines.First());
                lastLines.Add(lines.Last());
            }

            // Häufigste Kopf-/Fußzeilen bestimmen
            string header = FindRepeatedLine(firstLines);
            string footer = FindRepeatedLine(lastLines);

            Console.WriteLine($"[DEBUG] Erkannter Header: {header}");
            Console.WriteLine($"[DEBUG] Erkannter Footer: {footer}");

            var cleanedPages = new List<string>();

            foreach (var page in pages)
            {
                var lines = page.Split('\n')
                                .Select(l => l.Trim())
                                .ToList();

                // Entferne Header/Footer
                lines = lines.Where(l =>
                    !string.Equals(l, header, StringComparison.OrdinalIgnoreCase) &&
                    !string.Equals(l, footer, StringComparison.OrdinalIgnoreCase)
                ).ToList();

                // Entferne Seitenzahlen
                lines = lines.Where(l => !Regex.IsMatch(l, @"^Seite\s+\d+(\s+von\s+\d+)?$")).ToList();

                // Entferne Bildplatzhalter (OCR erzeugt oft sowas)
                lines = lines.Where(l => !Regex.IsMatch(l, @"^

\[.*Bild.*\]

$", RegexOptions.IgnoreCase)).ToList();

                cleanedPages.Add(string.Join("\n", lines));
            }

            var result = string.Join("\n\n", cleanedPages);

            Console.WriteLine("[DEBUG] DocumentCleaner: Reinigung abgeschlossen.");
            Console.WriteLine($"[DEBUG] Zeichen nach Reinigung: {result.Length}");

            return result;
        }

        private string FindRepeatedLine(List<string> lines)
        {
            return lines
                .GroupBy(l => l)
                .OrderByDescending(g => g.Count())
                .Where(g => g.Count() > lines.Count * 0.7) // >70% der Seiten
                .Select(g => g.Key)
                .FirstOrDefault() ?? "";
        }
    }
}
