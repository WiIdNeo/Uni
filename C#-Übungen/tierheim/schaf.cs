namespace tierheim
{
    public class Schaf : Tier
    {
        private static readonly string[] Sounds =
        {
            "Määäh!",
            "Mäh!",
            "Möööh!"
        };

        private static Random _rand = new Random();

        public Schaf()
        {
            Terrain = "Weide";
            HungryAfter = TimeSpan.FromSeconds(70);
            IsHealthy = true;
        }

        public override void MakeNoise()
        {
            Console.WriteLine($"{Name} blökt: {Sounds[_rand.Next(Sounds.Length)]}");
        }

        public void GiveWool()
        {
            Console.WriteLine($"{Name} wurde geschoren und gibt Wolle!");
        }
    }
}
