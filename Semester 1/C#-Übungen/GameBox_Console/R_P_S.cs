using GameBox;

namespace GameBox
{
    class R_P_S
    {
        static void RPS()
        {
            int wins = 0;
            int losts = 0;
            int rounds;
            Console.WriteLine("Welcome to RPS. How many rounds do you want to play?\n");
            x = Console.ReadLine();
            if (!int.TryParse(x, out rounds))
            {
                Console.WriteLine("Ungültige eingabe...\n\n\n");
            }
            else
            {
                for (int i = 0; i < rounds; i++)
                {
                    Console.WriteLine("Was setzt du?\n1) Rock\n2) Paper\n3) Scissor\n");
                    x = Console.ReadLine();
                    string y = GameMenu.RandNum(1, 4);
                    char result = Vali(x, y);
                    switch (result)
                    {
                        case 'w':
                            wins++;
                            Console.WriteLine($"You won this round!\n Wins: {wins} : Losts {losts}\n\n");
                            break;
                        case 'l':
                            losts++;
                            Console.WriteLine($"You lost this round!\n Wins: {wins} : Losts {losts}\n\n");
                            break;
                        case 'r':
                            Console.WriteLine($"Remee!\n Wins: {wins} : Losts {losts}\n\n");
                            break;
                        default:
                            Console.WriteLine("No valid input, try again!");
                            i--;
                    }
                }
                Console.WriteLine($"\n\nGame End!\nWins : Losts\n  {wins} : {losts}\n");
                Console.WriteLine(wins < losts ? "You lost!" : wins == losts ? "Remee!" : "You won!");
                Console.WriteLine("\n\n");

            }



        }
        private static char Vali(int x, int y)
        {
            switch (x)
            {
                case 1:
                    switch (y)
                    {
                        case 1:
                            return 'r';
                        case 2:
                            return 'l';
                        case 3:
                            return 'w';
                    }
                case 2:
                    switch (y)
                    {
                        case 1:
                            return 'w';
                        case 2:
                            return 'r';
                        case 3:
                            return 'l';
                    }
                case 1:
                    switch (y)
                    {
                        case 1:
                            return 'l';
                        case 2:
                            return 'w';
                        case 3:
                            return 'r';
                    }
            }
        }
    }
}