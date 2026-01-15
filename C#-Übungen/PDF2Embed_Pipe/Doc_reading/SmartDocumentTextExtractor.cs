using System;
using System.IO;
using System.Threading.Tasks;

namespace DocumentIngestion
{
    public class SmartDocumentTextExtractor : IDocumentTextExtractor
    {
        private readonly PdfTextExtractor _pdfExtractor;
        private readonly TesseractOcrExtractor _ocrExtractor;

        public SmartDocumentTextExtractor(PdfTextExtractor pdfExtractor, TesseractOcrExtractor ocrExtractor)
        {
            _pdfExtractor = pdfExtractor;
            _ocrExtractor = ocrExtractor;
        }

        public async Task<string> ExtractTextAsync(string filePath)
        {
            Console.WriteLine($"[DEBUG] SmartDocumentTextExtractor: Starte Extraktion für {filePath}");

            var ext = Path.GetExtension(filePath).ToLowerInvariant();

            if (ext == ".pdf")
            {
                var text = _pdfExtractor.Extract(filePath);

                if (text.Length < 50)
                {
                    Console.WriteLine("[DEBUG] SmartDocumentTextExtractor: PDF enthält kaum Text → OCR wird verwendet.");
                    return await _ocrExtractor.ExtractAsync(filePath);
                }

                Console.WriteLine("[DEBUG] SmartDocumentTextExtractor: PDF enthält Text → OCR nicht nötig.");
                return text;
            }

            if (ext is ".jpg" or ".jpeg" or ".png" or ".tif" or ".tiff")
            {
                Console.WriteLine("[DEBUG] SmartDocumentTextExtractor: Bilddatei erkannt → OCR wird verwendet.");
                return await _ocrExtractor.ExtractAsync(filePath);
            }

            throw new NotSupportedException($"Dateityp {ext} wird nicht unterstützt.");
        }
    }
}
