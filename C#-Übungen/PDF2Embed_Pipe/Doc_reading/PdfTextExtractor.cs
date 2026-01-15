using System;
using System.Text;
using UglyToad.PdfPig;

namespace DocumentIngestion
{
    public class PdfTextExtractor
    {
        public string Extract(string filePath)
        {
            Console.WriteLine($"[DEBUG] PdfTextExtractor: Öffne PDF: {filePath}");

            var sb = new StringBuilder();

            using var document = PdfDocument.Open(filePath);
            Console.WriteLine($"[DEBUG] Seiten im PDF: {document.NumberOfPages}");

            foreach (var page in document.GetPages())
            {
                Console.WriteLine($"[DEBUG] Lese Seite {page.Number}...");
                sb.AppendLine(page.Text);
                sb.AppendLine("\n--- PAGE BREAK ---\n");
            }

            var text = sb.ToString();
            Console.WriteLine($"[DEBUG] PdfTextExtractor: Extrahierte Zeichen: {text.Length}");

            return text;
        }
    }
}
