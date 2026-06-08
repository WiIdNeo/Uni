namespace ConsoleRPG
{
    class Strand : Biom
    {
        public Strand()
        {
            encounters[0, 1] = 0.3;
            encounters[1, 1] = 0.2;
            encounters[2, 1] = 0.0;
            encounters[3, 1] = 0.2;
            encounters[4, 1] = 0.0;
            encounters[5, 1] = 0.3;
        } 
        public void StrandEventNothing()
        {
            Console.WriteLine("Nothing happend: May you just proceed...\n");
        }
        public void StrandNPC1()
        {
            Console.WriteLine("You meet an captain, which is offering you to keep you with them for 3 Coins. Wanna go?\n1) Yes\n2) No\n");
            x = Console.ReadLine();
            switch (x)
            {
                case 1:
                    Travel("Strand");
                    break;
                default:
                    Console.WriteLine("The ship sails without you...\n");
            }
        }
        public void StrandNPC2()
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
        public void StrandEnemy1()
        {
            y  = Bantits("Strand"); // Implement Bandits as enemies, addtional implement random for bandits
            Console.WriteLine($"A group of {y[2]} pirates invaded! \nThey want your stuff and so attack you!");
            Fight("bandits", "Strand",  y[2]); // number of bandits
            
        }
        public void StrandEnemy2()
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
        public void StrandEnviroment()
        {
            y = Bandits("Wave");
            Console.WriteLine($"You walk along the strand, but suddently a big wave catches you and pull you to ocean. \nOn your heavy attempts to get back to land you loose {y[1]}, but you survive! \n");
        }
    }
}
