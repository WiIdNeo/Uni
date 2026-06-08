namespace tierheim
{
    public class Kuh : Tier
    {
        private static readonly string[] Sounds =
        {
            "Muuuh!",
            "Muuuu!",
            "Möööh?"
        };

        private static Random _rand = new Random();

        public Kuh()
        {
            Terrain = "Weide";
            HungryAfter = TimeSpan.FromSeconds(90);
            IsHealthy = true;
        }

        public override void MakeNoise()
        {
            Console.WriteLine($"{Name} muht: {Sounds[_rand.Next(Sounds.Length)]}");
        }

        public void GiveMilk()
        {
            Console.WriteLine($"{Name} gibt frische Milch!");
        }
    }
}
