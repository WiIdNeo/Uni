using System.Text.Json;

namespace ConsoleRPG
{
    class SafeLoad
    {
        public Entity AddEntity(Entity newChar)
        {
            string json = File.ReadAllText("Safe.json");
            List<Entity> characters = JsonSerializer.Deserialize<List<Entity>>(json);
            characters.Add(newChar);

            var activeChar = characters.FirstOrDefault(c => c.Name == newChar.Name);
            return activeChar;
        }
        public static void Safe()
        {
            var options = new JsonSerializerOptions { WriteIndented = true };

            string json = JsonSerializer.Serialize(characters, options);
            File.WriteAllText("Safe.json", json);

        }
        public static Entity LoadEntity()
        {
            string json = File.ReadAllText("Safe.json");
            List<Entity> characters = JsonSerializer.Deserialize<List<Entity>>(json);

            Console.WriteLine("Speicherstände zu folgenden Charakteren gefunden:\n");

            foreach (var character in characters)
            {
                Console.WriteLine(character.Name + "\n");
            }
            while (true)
            {
                Console.WriteLine("Choose one of those Characters by entering its name: ");
                string input = Console.ReadLine();

                try 
                {
                    var activeChar = characters.FirstOrDefault(c => c.Name == input);
                }
                catch 
                {
                    continue;
                }

                return activeChar;
            }
            
        }

    }
}