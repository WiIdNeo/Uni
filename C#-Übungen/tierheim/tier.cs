namespace tierheim
{
    public class Tier
    {
        public string Name { get; set; }
        public string Terrain { get; set; }
        public int Age { get; set; }
        public bool IsHealthy { get; set; }
        public bool IsHungry { get; set; }

        public DateTime LastFed { get; set; } = DateTime.Now - TimeSpan.FromSeconds(59);
        public TimeSpan HungryAfter { get; set; } = TimeSpan.FromSeconds(60);

        public int GoesToBed { get; set; }
        public bool IsSleeping { get; set; }
        public int NoiceTrigger { get; set; }

        public virtual void MakeNoise()
        {
            Console.WriteLine($"{Name} makes an undefined noise.");
        }
    }
}
