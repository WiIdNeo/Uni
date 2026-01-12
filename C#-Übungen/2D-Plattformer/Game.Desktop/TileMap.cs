using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;

namespace Game.Desktop
{
    public class TileMap
    {
        private readonly string[] _collisionLayer;
        private readonly int _tileSize;

        public int Width => _collisionLayer[0].Length;
        public int Height => _collisionLayer.Length;
        public int TileSize => _tileSize;

        public TileMap(LevelData data)
        {
            _tileSize = data.TileSize;
            _collisionLayer = data.Layers["collision"];
        }

        public void Draw(SpriteBatch spriteBatch, Texture2D pixel)
        {
            for (int y = 0; y < Height; y++)
            {
                for (int x = 0; x < Width; x++)
                {
                    char tile = _collisionLayer[y][x];

                    if (tile == '#')
                    {
                        var rect = new Rectangle(
                            x * _tileSize,
                            y * _tileSize,
                            _tileSize,
                            _tileSize
                        );

                        spriteBatch.Draw(pixel, rect, Color.DarkGray);
                    }
                }
            }
        }
    }
}
