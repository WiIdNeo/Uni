using System;
using System.Diagnostics;
using System.IO;
using System.Text;
using System.Threading.Tasks;

namespace DocumentIngestion
{
    public class TesseractOcrExtractor
    {
        private readonly string _tesseractPath;
        private readonly string _languages;

        public TesseractOcrExtractor(string tesseractPath, string languages = "deu+eng")
        {
            _tesseractPath = tesseractPath;
            _languages = languages;
        }

        public async Task<string> ExtractAsync(string filePath)
        {
            Console.WriteLine($"[DEBUG] TesseractOcrExtractor: Starte OCR für: {filePath}");

            var tempBase = Path.Combine(Path.GetTempPath(), "tesseract_" + Guid.NewGuid().ToString("N"));
            var psi = new ProcessStartInfo
            {
                FileName = _tesseractPath,
                Arguments = $"\"{filePath}\" \"{tempBase}\" -l {_languages} --psm 1",
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                CreateNoWindow = true
            };

            using var process = Process.Start(psi);
            if (process == null)
                throw new Exception("Konnte Tesseract nicht starten.");

            var stdout = await process.StandardOutput.ReadToEndAsync();
            var stderr = await process.StandardError.ReadToEndAsync();

            Console.WriteLine("[DEBUG] TesseractOcrExtractor STDOUT:");
            if (!string.IsNullOrWhiteSpace(stdout))
                Console.WriteLine(stdout);

            Console.WriteLine("[DEBUG] TesseractOcrExtractor STDERR:");
            if (!string.IsNullOrWhiteSpace(stderr))
                Console.WriteLine(stderr);

            await process.WaitForExitAsync();

            var txtPath = tempBase + ".txt";
            if (!File.Exists(txtPath))
            {
                Console.WriteLine("[DEBUG] TesseractOcrExtractor: Keine Ausgabe-Datei gefunden – OCR fehlgeschlagen?");
                return string.Empty;
            }

            var text = await File.ReadAllTextAsync(txtPath, Encoding.UTF8);
            Console.WriteLine($"[DEBUG] TesseractOcrExtractor: Extrahierte Zeichen: {text.Length}");

            try
            {
                File.Delete(txtPath);
            }
            catch
            {
                // Nicht kritisch, wenn Temp-Datei liegen bleibt
            }

            return text;
        }
    }
}
