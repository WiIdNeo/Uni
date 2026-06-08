using System.Security.Cryptography.X509Certificates;

namespace sortLetters
{
    class SortAlgorythmLetters
    {
        static void Main(string []args)
        {
            Console.WriteLine("Welches Wort soll sortiert werden?");
            string input = Console.ReadLine();
            List<Char> word = input.ToList();
            word = RemoveSpecialLetters(word);
            Console.WriteLine($"\nBereinigtes Wort: {new string(word.ToArray())}\n");
            word = SortWord(word);
            


        }
        static List<char> ToLowerCase(List<char> word)
{
    for (int i = 0; i < word.Count; i++)
    {
        switch (word[i])
        {
            case 'A': word[i] = 'a'; break;         // char = ''
            case 'B': word[i] = 'b'; break;         // string = ""
            case 'C': word[i] = 'c'; break;
            case 'D': word[i] = 'd'; break;
            case 'E': word[i] = 'e'; break;
            case 'F': word[i] = 'f'; break;
            case 'G': word[i] = 'g'; break;
            case 'H': word[i] = 'h'; break;
            case 'I': word[i] = 'i'; break;
            case 'J': word[i] = 'j'; break;
            case 'K': word[i] = 'k'; break;
            case 'L': word[i] = 'l'; break;
            case 'M': word[i] = 'm'; break;
            case 'N': word[i] = 'n'; break;
            case 'O': word[i] = 'o'; break;
            case 'P': word[i] = 'p'; break;
            case 'Q': word[i] = 'q'; break;
            case 'R': word[i] = 'r'; break;
            case 'S': word[i] = 's'; break;
            case 'T': word[i] = 't'; break;
            case 'U': word[i] = 'u'; break;
            case 'V': word[i] = 'v'; break;
            case 'W': word[i] = 'w'; break;
            case 'X': word[i] = 'x'; break;
            case 'Y': word[i] = 'y'; break;
            case 'Z': word[i] = 'z'; break;
        }
    }
    return word;
}

        static List<char> RemoveSpecialLetters(List<char> word)
{
    for (int i = 0; i < word.Count; i++)
    {
        switch (word[i])
        {
            case 'ß':
                word[i] = 's';
                word.Add('s');
                break;

            case 'Ä':
            case 'ä':
                word[i] = 'a';
                word.Add('e');
                break;

            case 'Ö':
            case 'ö':
                word[i] = 'o';
                word.Add('e');
                break;

            case 'Ü':
            case 'ü':
                word[i] = 'u';
                word.Add('e');
                break;
        }
    }

    return ToLowerCase(word);
}

        static List<Char> SortWord(List<Char> word)
        {
            Char[] letters = { 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' };
            Char x = "";
            bool changed = true;
            while (changed == true)
            {
                changed = false;
                for (int i = 0; i < word.Count-1; i++)
                {
                    if (Array.IndexOf(letters, word[i]) > Array.IndexOf(letters, word[i+1])) //Umweg über Array unnötig
                    {                                                                       // C# kennt 'a' < 'b'
                        x = word[i];
                        word[i] = word[i+1];
                        word[i+1] = x;
                        changed = true;
                    }
                }
            }
            return word;
        }

    }    

}
