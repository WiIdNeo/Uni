using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;

namespace Game.Desktop
{
    public abstract class Entity
    {
        // Position & Bewegung
        public Vector2 Position;
        public Vector2 Velocity;
        public int Size;

        // Ressourcen
        public int MaxHP = 100;
        public int HP = 100;
        public int MaxMana = 50;
        public int Mana = 50;

        // Status Flags
        public bool OnGround = false;
        public bool IsFalling = false;
        public bool IsJumping = false;

        protected Entity(Vector2 position, int size)
        {
            Position = position;
            Size = size;
            Velocity = Vector2.Zero;
        }

        // Update-Logik (Input / KI / Angriff), Physics extern
        public abstract void Update(GameTime gameTime, TileMap tileMap);

        // Draw: nur Sprite/Hitbox, kein Physics
        public virtual void Draw(SpriteBatch spriteBatch, Texture2D pixel, Color color)
        {
            spriteBatch.Draw(pixel, new Rectangle((int)Position.X, (int)Position.Y, Size, Size), color);
        }

        // Leben/Status
        public virtual void TakeDamage(int amount)
        {
            HP -= amount;
            if (HP < 0) HP = 0;
        }

        public virtual void Heal(int amount)
        {
            HP += amount;
            if (HP > MaxHP) HP = MaxHP;
        }

        public virtual bool UseMana(int amount)
        {
            if (Mana >= amount)
            {
                Mana -= amount;
                return true;
            }
            return false;
        }
    }
}
