using System.Collections.Generic;

namespace Game.Desktop
{
    public class LevelData
    {
        public int TileSize { get; set; }
        public Dictionary<string, string[]> Layers { get; set; }
    }
}
