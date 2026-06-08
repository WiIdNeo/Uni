using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace DocumentIngestion
{
    public class DocumentDirectoryScanner
    {
        private readonly IDocumentTextExtractor _extractor;

        public DocumentDirectoryScanner(IDocumentTextExtractor extractor)
        {
            _extractor = extractor;
        }

        public async Task ProcessDirectoryAsync(string rootFolder)
        {
            Console.WriteLine($"[DEBUG] Starte Ordnerscan: {rootFolder}");

            if (!Directory.Exists(rootFolder))
            {
                Console.WriteLine("[DEBUG] Ordner existiert nicht!");
                return;
            }

            var supportedExtensions = new HashSet<string>(StringComparer.OrdinalIgnoreCase)
            {
                ".pdf", ".jpg", ".jpeg", ".png", ".tif", ".tiff"
            };

            var files = Directory
                .EnumerateFiles(rootFolder, "*.*", SearchOption.AllDirectories)
                .Where(f => supportedExtensions.Contains(Path.GetExtension(f)));

            int count = 0;

            foreach (var file in files)
            {
                count++;
                Console.WriteLine($"[DEBUG] [{count}] Verarbeite Datei: {file}");

                try
                {
                    var text = await _extractor.ExtractTextAsync(file);

                    Console.WriteLine($"[DEBUG] Extrahierte Zeichen: {text.Length}");
                    Console.WriteLine("---------- EXTRAHIERTER TEXT (ANFANG) ----------");

                    var preview = text.Length > 500 ? text[..500] + "..." : text;
                    Console.WriteLine(preview);

                    Console.WriteLine("---------- EXTRAHIERTER TEXT (ENDE) ------------");
                    Console.WriteLine();
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"[DEBUG] Fehler bei Datei {file}: {ex.GetType().Name} - {ex.Message}");
                }
            }

            Console.WriteLine($"[DEBUG] Fertig. Insgesamt verarbeitete Dateien: {count}");
        }
    }
}
