using System;
using System.Threading.Tasks;

namespace DocumentIngestion
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;

            Console.WriteLine("===== Dokument-Ingestion Prototyp =====");

            string rootFolder;
            if (args.Length > 0)
            {
                rootFolder = args[0];
            }
            else
            {
                Console.Write("Bitte Wurzelordner eingeben: ");
                rootFolder = Console.ReadLine() ?? string.Empty;
            }

            if (string.IsNullOrWhiteSpace(rootFolder))
            {
                Console.WriteLine("Kein Ordner angegeben. Beende.");
                return;
            }

            var pdfExtractor = new PdfTextExtractor();

            var tesseractPath = @"C:\Program Files\Tesseract-OCR\tesseract.exe"; // ggf. anpassen
            var ocrExtractor = new TesseractOcrExtractor(tesseractPath, "deu+eng");

            var smartExtractor = new SmartDocumentTextExtractor(pdfExtractor, ocrExtractor);
            var scanner = new DocumentDirectoryScanner(smartExtractor);

            try
            {
                await scanner.ProcessDirectoryAsync(rootFolder);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Unerwarteter Fehler:");
                Console.WriteLine(ex);
            }

            Console.WriteLine("===== Fertig. Taste drücken zum Beenden. =====");
            Console.ReadKey();
        }
    }
}
