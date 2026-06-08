using ConsoleRPG.Entity;
using ConsoleRPG.Program;

namespace ConsoleRPG 
{
    public class Player : Entity
    {
        public Player() 
        {

            Name = "";
            Profession = "";
            Level = 1;
            Exp = 0;
            HP = 100;
            BaseDamage = 10;
            MagicDamage = 10;
            BaseDefense = 5;
            MagicDefense = 5;
            Endurance = 20;
            currentEndurance = 20;
            Dex = 10;
            Mana = 10;
            currentMana = 10;
            PlayersTeam = true;
            MaxLoad = 10;
            int[] currentPosition = {1, 2};
            currentPosition[0] = 
            currentPosition[1] = rnd.Next(1, 8);
        }
        
    }

}