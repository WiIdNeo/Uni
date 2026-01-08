namespace tierheim
{
    public class Hund : Tier
    {
        private static readonly string[] Sounds = 
        {
            "Wuff!", 
            "Wau!", 
            "Grrrr!", 
            "Wuff-wuff!"
        };

        private static Random _rand = new Random();

        public Hund()
        {
            Terrain = "Land";
            HungryAfter = TimeSpan.FromSeconds(60); // Hunde werden nach 60s hungrig
            IsHealthy = true;
        }

        public override void MakeNoise()
        {
            int index = _rand.Next(Sounds.Length);
            Console.WriteLine($"{Name} says: {Sounds[index]}");
        }

        public void FetchStick()
        {
            Console.WriteLine($"{Name} holt begeistert einen Stock!");
        }
    }
}
