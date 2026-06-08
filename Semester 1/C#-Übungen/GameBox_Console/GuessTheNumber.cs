using GameBox;

namespace GameBox
{
    class GTN
    {
        public void GuessTheNumber()
        {
            bool Correct = false;
            Console.WriteLine("Welcome to Guess the NUmber! \nYour task is to guess a random number in 5 Attempts. \nFirst select a difficulty:\n1) Easy\n2) Medium\n3) Hard\n");
            string y = Console.ReadLine();
            int Num = RandNum(1, y == "1" ? 10 
            : y=="2" ? 100 
            : 1000
            );
            for (int i = 0; i < 5 && !Correct; i++)
            {
                Console.WriteLine($"What is your {i+1}. guess?\n");
                x = Console.ReadLine();
                if (x == Num)
                {
                    Console.WriteLine("That's correct! Congratulation!\n");
                    Correct == true;
                }
                else
                {
                    Console.WriteLine(x < Num ? "The number is bigger... \n" : "The number is smaller...\n");
                }
                if (!Correct && i == 4)
                {
                    Console.WriteLine("You didn't made it. Better Luck next time!\n\n");
                }
            }
        }
    }
}