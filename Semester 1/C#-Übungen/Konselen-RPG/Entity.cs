namespace ConsoleRPG 
{
    public class Entity
    {
        
        public string Name { get; set; }
        public string Profession { get; set; }
        public int Level { get; set; }
        public int Exp { get; set; }
        public int HP { get; set; }
        public int BaseDamage { get; set; }
        public int MagicDamage { get; set; }
        public int BaseDefense { get; set; }
        public int MagicDefense { get; set; }
        public int Endurance { get; set; }
        public int Dex { get; set; }
        public int currentEndurance {get; set;}
        public int Mana { get; set; }
        public int currentMana { get; set; }
        public bool PlayersTeam { get; set; }

        public List<string> Inventory { get; set; } = new List<string>();
        public int coins { get; set; } = 0;
        public int MaxLoad { get; set; } = 3;
    }

}