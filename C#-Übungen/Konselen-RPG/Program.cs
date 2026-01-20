using ConsoleRPG.SafeLoad;

namespace ConsoleRPG
{
    class Program
    {
        public static void Main(string []args)
        {
            while (true)
            {
                // Menue Screen
                Console.WriteLine("What to do? \n1) Load Charater\n2) Create New Character\n3) Credits\n4) Leave Game\n");
                x = Console.ReadLine();
                switch (x) 
                {
                    case 1:
                        var activeChar = SafeLoad.LoadEntity();
                        GameScreen(activeChar);
                        break;
                    case 2:
                        var activeChar = CreateScreen();
                        GameScreen(activeChar);
                        break;
                    case 3:
                        SafeLoad.LoadCredits(); //noch erstellen
                        break;
                    case 4:
                        return;
                    default: 
                        continue;
                } 

                
            }
        }
        public static Entity CreateScreen()
        {
            Console.WriteLine("Welcome to Character Creation: \n\nFirst enter a name: ");
            string x = Console.ReadLine();
            Console.WriteLine($"\nWich Prefession does {x} belong to?\n1) Warrior\n2) Mage\n");
            string y = Console.ReadLine();
            switch (y)
            {
                case 1:
                    y = "Warrior";
                    break;
                case 2:
                    y = "Mage";
                    break;
            }

            Player newChar = new Player();
            newChar.Name = x;
            newChar.Profession = y;
            var activeChar = SafeLoad.AddEntity(newChar);

            return activeChar;
        }

        public static void GameScreen()
        {
            while (true)
            {
                World.Prompt(currentPosition);

            }
        }
        
        Random rnd = new Random();
        public static int Rand(int min, int max)
        {
            return rnd.Next(min, max + 1);
        }


    }    
}
