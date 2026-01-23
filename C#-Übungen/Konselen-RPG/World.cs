using ConsoleRPG;
namespace ConsoleRPG
{
    class World
    {
        static void Prompt(int[] position)
        {
            int[,] map = new int[,]
            {
                {0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 1, 1, 1, 9, 2, 2, 2, 0},
                {0, 1, 1, 2, 2, 2, 2, 2, 0},
                {0, 2, 2, 2, 2, 3, 3, 3, 0},
                {0, 9, 2, 2, 3, 3, 3, 3, 0},
                {0, 2, 2, 3, 3, 3, 3, 3, 0},
                {0, 2, 5, 2, 3, 3, 3, 3, 0},
                {0, 2, 5, 2, 9, 2, 2, 2, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0}
            };

            string currentBiom = map[position[0]][position[1]];
            switch (currentBiom)
            {
                case "1":
                    getEvent("Strand");
                    break;
                case "2":
                    currentBiom = "Meadow";
                    break;
                case "3":
                    currentBiom = "Woods";
                    break;
                case "9":
                    currentBiom = "City";
                    break;
            }
                

        }  
        static void getEvent(string x)
        {
            encounters[0, 1] = 0.35;
            encounters[1, 1] = 0.1;
            encounters[2, 1] = 0.1;
            encounters[3, 1] = 0.2;
            encounters[4, 1] = 0.25;
            encounters[5, 1] = 0.0;
            int y = Program.Rand(1, 100);
            if (y > 7)
            {
                
            }
        }
    }
}