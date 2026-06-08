namespace tierheim
{
    public class Huhn : Tier
    {
        private static readonly string[] Sounds =
        {
            "Gack!",
            "Gack-gack!",
            "Kikeriki!"
        };

        private static Random _rand = new Random();

        public Huhn()
        {
            Terrain = "Hof";
            HungryAfter = TimeSpan.FromSeconds(30);
            IsHealthy = true;
        }

        public override void MakeNoise()
        {
            Console.WriteLine($"{Name} gackert: {Sounds[_rand.Next(Sounds.Length)]}");
        }

        public void LayEgg()
        {
            Console.WriteLine($"{Name} hat ein Ei gelegt!");
        }
    }
}
