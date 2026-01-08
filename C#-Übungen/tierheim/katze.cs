namespace tierheim
{
    public class Katze : Tier
    {
        private static readonly string[] Sounds =
        {
            "Miau!",
            "Mrrr...",
            "Hiss!",
            "Miau-miau!"
        };

        private static Random _rand = new Random();

        public Katze()
        {
            Terrain = "Hof";
            HungryAfter = TimeSpan.FromSeconds(45);
            IsHealthy = true;
        }

        public override void MakeNoise()
        {
            Console.WriteLine($"{Name} sagt: {Sounds[_rand.Next(Sounds.Length)]}");
        }

        public void Scratch()
        {
            Console.WriteLine($"{Name} kratzt an einem Holzpfosten!");
        }
    }
}
