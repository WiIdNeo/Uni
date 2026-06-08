namespace ConsoleRPG
{
    class Meadows : Biom
    {
        public Meadows()
        {
            encounters[0, 1] = 0.35;
            encounters[1, 1] = 0.1;
            encounters[2, 1] = 0.1;
            encounters[3, 1] = 0.2;
            encounters[4, 1] = 0.25;
            encounters[5, 1] = 0.0;
        } 
        public void MeadowEventNothing()
        {
            Console.WriteLine("Nothing happend: May you just proceed...\n");
        }
        public void MeadowNPC1()
        {
            Console.WriteLine("You meet an Merchant, wanna buy something? \n1) Yes, show me your stuff. \n2) No, good bye.\n");
            x = Console.ReadLine();
            switch (x)
            {
                case 1:
                    Merchant("Grassland"); // Implement Merchant Funktion
                    break;
                default:
                    Console.WriteLine("The merchant Left...\n");
            }
        }
        public void MeadowNPC2()
        {
            Console.WriteLine("You meet a karawan, they offer you to take you with them to next City for 2 Coins\n1) Yes, thanks!\n2) No, thanks anyway.\n");
            x = Console.ReadLine();
            switch (x)
            {
                case 1:
                    Travel("karawan"); // Implement Travel Funktion
                    break;
                default:
                    Console.WriteLine("The karawan passed...\n");
            }
        }
        public void MeadowEnemy1()
        {
            y  = Bantits("Grassland"); // Implement Bandits as enemies, addtional implement random for bandits
            Console.WriteLine($"A group of {y[2]} bandits invaded! \nThey want you to pay {y[0]} and additional give them your {y[1]} \nDo you\n1) pay or \n2) fight?");
            x = Console.ReadLine();
            switch (x)
            {
                case 1:
                    SellItems(y[1], 0); // item to leave
                    buyItems("", y[0]); // amount of Coins to leave
                    break;
                default:
                    Fight("bandits", "Grassland",  y[2]); // number of bandits
            }
        }
        public void MeadowEnemy2()
        {
            y = Wolfes("Grassland");
            Console.WriteLine($"In small distance you spott a group of {y[2]} wolfes. \nWhat do you want to do? \n1) Try to escape, maybe they didn't noticed you yet.\n2) Face the wolfes and see if they attack.");
            x = Console.ReadLine();
            switch (x)
            {
                case 1:
                    if (y[0])
                    {
                        Console.WriteLine("You were lucky, you got the escape!\n");
                        //zufällige bewegungsrichtung
                    }
                    else
                    {
                        Console.WriteLine("Very unlicky: The wolfes already got your path and hunt you down!\n");
                        Fight("wolfes", "Grassland", y[2]);
                    }
                    break;
                case 2:
                    Console.WriteLine("You move closer to the wolfes, just headding your way. And the wolfes...");
                    if (y[1])
                    {
                        Console.WriteLine("... start to attack!\n");
                        Fight("wolfes", "Grassland", y[2]);
                    }
                    else
                    {
                        Console.WriteLine("...run away!\n");
                    }

            }
        }
        public void MeadowEnviroment()
        {
            // nothing will happen...
        }
    }
}
