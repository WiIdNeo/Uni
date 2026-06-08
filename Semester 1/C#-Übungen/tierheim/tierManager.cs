namespace tierheim
{
    public class TierManager
    {
        private List<Tier> _tiere = new();
        public IReadOnlyList<Tier> Tiere => _tiere;

        private Random _rand = new Random();
        private System.Timers.Timer _timer;

        public TierManager()
        {
            _timer = new System.Timers.Timer(1000);
            _timer.Elapsed += Tick;
            _timer.Start();
        }

        private void Tick(object sender, EventArgs e)
        {
            foreach (var tier in _tiere)
            {
                // Geräusche
                tier.NoiceTrigger += _rand.Next(1, 10);
                if (tier.NoiceTrigger >= 75)
                {
                    tier.NoiceTrigger = 0;
                    tier.MakeNoise();
                }

                // Schlafen
                if (!tier.IsSleeping)
                {
                    tier.GoesToBed += _rand.Next(1, 5);

                    if (tier.GoesToBed >= 250)
                    {
                        tier.IsSleeping = true;
                        Console.WriteLine($"{tier.Name} is now sleeping!");
                    }
                }
                else
                {
                    tier.LastFed = DateTime.Now - (tier.HungryAfter - TimeSpan.FromSeconds(3));
                    tier.GoesToBed -= _rand.Next(1, 5);

                    if (tier.GoesToBed <= 0)
                    {
                        tier.IsSleeping = false;
                        Console.WriteLine($"{tier.Name} just woke up!");
                    }
                }

                // Hunger
                if (!tier.IsHungry && DateTime.Now - tier.LastFed > tier.HungryAfter)
                {
                    tier.IsHungry = true;
                    Console.WriteLine($"{tier.Name} ist jetzt hungrig!");
                }
            }
        }

        public void AddTier(Tier t)
        {
            _tiere.Add(t);
        }
    }
}
