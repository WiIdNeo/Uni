using ConsoleRPG;

namespace ConsoleRPG
{
    class Wood : Biom
    {
        public Wood()
        {
            encounters[0, 1] = 0.25;
            encounters[1, 1] = 0.15;
            encounters[2, 1] = 0.1;
            encounters[3, 1] = 0.3;
            encounters[4, 1] = 0.1;
            encounters[5, 1] = 0.1;
        } 
        public void WoodsEventNothing()
        {
            Console.WriteLine("Nothing happend: May you just proceed...\n");
        }
        public void WoodsNPC1()
        {
            Console.WriteLine("You meet an Merchant, wanna buy something? \n1) Yes, show me your stuff. \n2) No, good bye.\n");
            x = Console.ReadLine();
            switch (x)
            {
                case 1:
                    Merchant("Woods"); // Implement Merchant Funktion
                    break;
                default:
                    Console.WriteLine("The merchant Left...\n");
            }
        }
        public void WoodsNPC2()
        {
            Console.WriteLine("You find a group of friendly dryads. They offer you a rest. \n");
            y = Rest("+");
            Console.WriteLine($"You rested at the dryads village. The graceful ambient make you recover {y[0]} HP and {y[1]} Mana. \n");
                    
        }
        public void WoodsEnemy1()
        {
            y  = MagicEnemy("Woods");
            Console.WriteLine($"You disturbt a group of Dryads going angry for this. They attack!");
            Fight("bandits", "Grassland",  y[2]);
            
        }
        public void WoodsEnemy2()
        {
            y = Bandits("Woods");
            Console.WriteLine($"You get prisoned by some Goblins. They want you to leave them your {y[0]} and a total of {y[1]} coins. Wanna pay them or try to rage your vessels? \n1) Try an escape.\n2) Pay them.\n");
            x = Console.ReadLine();
            int z = 0;
            switch (x)
            {
                case "1":
                {
                    if (Main.rand.ran.Next(z, 10) > 7)
                    {
                        Console.WriteLine("Your vessels actually broke...");
                        x = Console.ReadLine();
                        if (x == "1")
                        {
                            Inventory("Add", y[3]);
                        }
                    }
                    else
                    {
                        Console.WriteLine("For now the vessels doesn't break...");
                        z++;
                        activeChar.HP -= Main.rand(1, 3);

                        while (true)
                        {
                            Console.WriteLine("Your vessels feel less strong now...");
                            x = Console.ReadLine();

                            switch (x)
                            {
                                case "1":
                                    if (Main.rand.ran.Next(z, 10) > 7)
                                    {
                                        Console.WriteLine("Your vessels actually broke...");
                                        x = Console.ReadLine();
                                        if (x == "1")
                                        {
                                            Inventory("Add", y[3]);
                                        }
                                        break;
                                    }
                                    else
                                    {
                                        Console.WriteLine("For now the vessels doesn't break...");
                                        z++;
                                        activeChar.HP -= Main.rand(1, 3);
                                        continue;
                                    }
                            }
                            break;
                        }
                    }
                    break;   // ← WICHTIG! Case 1 sauber beenden
                }

                case "2":
                    Console.WriteLine("You Pay the goblins...");
                    SellItem(y[0], 0);
                    BuyItem("", y[1]);
                    break;
            }
        }

            
        public void MeadowEnviroment()
        {
            Console.WriteLine($"Suddently a ast is falling off a tree exactly on your Head. You get damaged for {Main.Rand(1, activeChar.HP)}\n");
        }
    }
}
