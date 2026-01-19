namespace palindrom
{
    class Palindrom
    {
        static void Main(string []args)
        {

            Console.WriteLine("Gib ein Wort ein, dass du prüfen möchtest: ");
            string x = Console.ReadLine();
            bool y = true;
            x = x.ToLower();

            for (int i = 0; i < x.Length/2; i++)
            {
                if (x[i] != x[^(i+1)])
                {
                    y = false;
                }
            }
            if (y)
            {
                Console.WriteLine($"{x} ist ein Palindrom!");
            }
            else
            {
                Console.WriteLine($"{x} ist kein Palindrom!");
            }

        }


    }    

}