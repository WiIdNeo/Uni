namespace ConsoleRPG
{
    class City : Biom
    {
        public Cities()
        {
            encounters[0, 1] = 0.15;
            encounters[1, 1] = 0.3;
            encounters[2, 1] = 0.2;
            encounters[3, 1] = 0.2;
            encounters[4, 1] = 0.15;
            encounters[5, 1] = 0.0;
        } 
        public void CityEventNothing()
        {
            Console.WriteLine("Nothing happend: May you just proceed...\n");
        }
        public void CityNPC1()
        {
            Console.WriteLine("There is a shop ahead, wanna go in and buy something?\n1) Yes. \n2) No.");
            x = Console.ReadLine();
            switch (x)
            {
                case 1:
                    Merchant("City"); // Implement Merchant Funktion
                    break;
                default:
                    Console.WriteLine("You just keep going...\n");
            }
        }
        public void CityNPC2()
        {
            Console.WriteLine("You spot a bank ahead, wanna depot something?\n1) Yes. \n2) No.\n");
            x = Console.ReadLine();
            switch (x)
            {
                case 1:
                    Merchant("bank");
                    break;
                default:
                    Console.WriteLine("You ignored the Bank.\n");
            }
        }
        public void CityEnemy1()
        {
            y  = Bantits("City"); // Implement Bandits as enemies, addtional implement random for bandits
            Console.WriteLine($"A group of {y[2]} bandits invaded! \nThey want you to pay {y[0]} and additional give them your {y[1]} \nDo you\n1) pay or \n2) fight?");
            x = Console.ReadLine();
            switch (x)
            {
                case 1:
                    SellItems(y[1], 0); // item to leave
                    buyItems("", y[0]); // amount of Coins to leave
                    Console.WriteLine("You paid the bandits and they let you pass...\n");
                    break;
                default:
                    Fight("bandits", "Grassland",  y[2]); // number of bandits
            }
        }
        public void CityEnemy2()
        {
            y = Rats("City");
            Console.WriteLine($"You walk through a dark side street and get faced by a few rats! \nWhat to do?\n1) Drop a random nurishment and run or \n2) Fight them?");
            x = Console.ReadLine();
            switch (x)
            {
                case 1:
                    SellItems(y[1], 0);
                    Console.WriteLine($"You dropped {y[1]} and got the escape!\n");
                    //zufällige bewegungsrichtung
                    break;
                case 2:
                    Console.WriteLine("You grapped your weapon harder ready for the Attack and the rats...");
                    if (y[1])
                    {
                        Console.WriteLine("... start to attack!\n");
                        Fight("rats", "City", y[2]);
                    }
                    else
                    {
                        Console.WriteLine("...run away!\n");
                    }

            }
        }
        public void CityEnviroment()
        {
            // nothing will happen...
        }
    }
}
