using Microsoft.Xna.Framework;

namespace Game.Desktop
{
    public class Camera
    {
        public Vector2 Position { get; private set; }
        public int ViewWidth { get; }
        public int ViewHeight { get; }

        public Camera(int viewWidth, int viewHeight)
        {
            ViewWidth = viewWidth;
            ViewHeight = viewHeight;
            Position = Vector2.Zero;
        }

        public void Follow(Vector2 target, int worldWidth, int worldHeight)
        {
            // Kamera zentrieren
            Position.X = target.X - ViewWidth / 2;
            Position.Y = target.Y - ViewHeight / 2;

            // Innerhalb der Weltgrenzen halten
            Position.X = MathHelper.Clamp(Position.X, 0, worldWidth - ViewWidth);
            Position.Y = MathHelper.Clamp(Position.Y, 0, worldHeight - ViewHeight);
        }

        public Matrix GetViewMatrix()
        {
            return Matrix.CreateTranslation(new Vector3(-Position, 0));
        }
    }
}
