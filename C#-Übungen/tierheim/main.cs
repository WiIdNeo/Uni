// Copyright (c) 2025 WiIdNeo
// This file is part of an open-source project licensed under the MIT License.
// You may use, modify, and distribute this file under the terms of the MIT License.
// Provided "as is", without warranty of any kind.
// See the LICENSE file for details.

using tierheim;

namespace tierheim
{
    class Program
    {
        static TierManager manager = new TierManager();
        static Random _rand = new Random();

        static List<Func<Tier>> _tierFactories = new()
        {
            () => new Katze(),
            () => new Schaf(),
            () => new Kuh(),
            () => new Huhn()
        };

        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("1) Tierstatus anzeigen");
                Console.WriteLine("2) Tier füttern");
                Console.WriteLine("3) Neues Tier aufnehmen");
                Console.WriteLine("4) Beenden");

                string input = Console.ReadLine();

                switch (input)
                {
                    case "1":
                        GetStateOf();
                        break;

                    case "2":
                        FeedPet();
                        break;

                    case "3":
                        CreatePet();
                        break;

                    case "4":
                        return;

                    default:
                        Console.WriteLine("Ungültige Eingabe.");
                        break;
                }
            }
        }

        static void CreatePet()
        {
            int index = _rand.Next(_tierFactories.Count);
            Tier neuesTier = _tierFactories[index]();

            Console.WriteLine($"Du bekommst ein neues Tier: {neuesTier.GetType().Name}!");

            Console.Write("Wie soll das Tier heißen? ");
            neuesTier.Name = Console.ReadLine();

            bool startHungry = _rand.Next(0, 2) == 1;
            if (startHungry)
            {
                neuesTier.LastFed = DateTime.Now - (neuesTier.HungryAfter - TimeSpan.FromSeconds(3));
                neuesTier.IsHungry = true;
            }
            else
            {
                neuesTier.LastFed = DateTime.Now;
            }

            neuesTier.IsSleeping = false;
            neuesTier.GoesToBed = _rand.Next(0, 200);

            manager.AddTier(neuesTier);

            Console.WriteLine($"{neuesTier.Name} ({neuesTier.GetType().Name}) wurde erfolgreich aufgenommen!\n");
        }

        static void GetStateOf()
        {
            foreach (var tier in manager.Tiere)
            {
                Console.WriteLine($"{tier.Name}:");
                Console.WriteLine($"  Art: {tier.GetType().Name}");
                Console.WriteLine($"  Terrain: {tier.Terrain}");
                Console.WriteLine($"  Hungrig: {tier.IsHungry}");
                Console.WriteLine($"  Schlafend: {tier.IsSleeping}\n");
            }
        }

        static void FeedPet()
        {
            Console.WriteLine("Welches Tier soll gefüttert werden?");
            string name = Console.ReadLine();

            var tier = manager.Tiere.FirstOrDefault(t => t.Name == name);

            if (tier == null)
            {
                Console.WriteLine("Tier nicht gefunden.");
                return;
            }

            tier.LastFed = DateTime.Now;
            tier.IsHungry = false;

            Console.WriteLine($"{tier.Name} wurde gefüttert!");
        }
    }
}
