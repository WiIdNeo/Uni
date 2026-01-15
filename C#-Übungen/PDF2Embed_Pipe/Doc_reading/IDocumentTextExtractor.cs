using System.Threading.Tasks;

namespace DocumentIngestion
{
    public interface IDocumentTextExtractor
    {
        Task<string> ExtractTextAsync(string filePath);
    }
}
