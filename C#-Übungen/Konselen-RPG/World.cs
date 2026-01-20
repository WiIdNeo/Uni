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
            int y = Program.Rand(1, 100);
        }
    }
}