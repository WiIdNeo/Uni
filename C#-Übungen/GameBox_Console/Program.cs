using GameBox.GuessTheNumber;


namespace GameBox
{
    class GameMenu
    {
        Random rnd = new Random();
        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("\n\nWelcome to Game Box! \nThis is your Game Hub to play different games. \nIn current version we got:\n 1) Guess the number\n 2) R-P-S"+
                 "\n 3) Hangman\n 4) Black Jack \n 5) Reaction Test\nWhat do you want to play?\n");
                string y = Console.ReadLine();
                switch (y)
                {
                    case "1":
                        GTN.GuessTheNumber();
                        break;
                    case "2":
                        R_P_S();
                        break;
                    case "3":
                        Hangman();
                    case "4": 
                        BlackJack();
                        break;
                    case "5":
                        ReactionTest();
                        break;
                    default:
                        Console.WriteLine("\n************************************\n No valid input! Restarting Menu...\n************************************\n");
                }
            }
        }
        static int RandNum(int min, int max)
        {
            int num = rnd.Next(min, max+1);
            return num;
        } 
    }
}