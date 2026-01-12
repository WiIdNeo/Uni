using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using System;

namespace Game.Desktop
{
    public class Player : Entity
    {
        // Bewegung
        public readonly float MoveSpeed = 150f;
        public readonly float JumpForce = 400f;
        public readonly float Gravity = 1000f;
        public readonly float FallMultiplier = 1.5f;
        public readonly float LowJumpMultiplier = 2f;
        public readonly float MaxFallSpeed = 600f;

        // Angriff
        private readonly int AttackDamage = 10;
        private readonly float AttackRange = 20f;
        private readonly float AttackCooldown = 0.5f;
        private readonly int AttackManaCost = 5;
        private float _attackTimer = 0f;

        public Player(Vector2 startPos, int size) : base(startPos, size) { }

        public override void Update(GameTime gameTime, TileMap tileMap)
        {
            float dt = (float)gameTime.ElapsedGameTime.TotalSeconds;

            // --- Input ---
            Vector2 input = Vector2.Zero;
            KeyboardState ks = Keyboard.GetState();
            if (ks.IsKeyDown(Keys.A) || ks.IsKeyDown(Keys.Left)) input.X = -1;
            if (ks.IsKeyDown(Keys.D) || ks.IsKeyDown(Keys.Right)) input.X = 1;

            // Update horizontal Velocity (Physics zentral später)
            Velocity.X = input.X * MoveSpeed;

            // Jump Input
            if (OnGround && ks.IsKeyDown(Keys.Space))
            {
                Velocity.Y = -JumpForce;
                OnGround = false;
                IsJumping = true;
            }

            // Angriff
            if (_attackTimer > 0f) _attackTimer -= dt;
            if (ks.IsKeyDown(Keys.F) && _attackTimer <= 0f && UseMana(AttackManaCost))
            {
                _attackTimer = AttackCooldown;
                PerformAttack();
            }
        }

        private void PerformAttack()
        {
            Console.WriteLine($"Attack! Damage: {AttackDamage}");
            // Später: Hitbox-Kollision prüfen
        }

        public override void Draw(SpriteBatch spriteBatch, Texture2D pixel, Color color = default)
        {
            base.Draw(spriteBatch, pixel, Color.Red);

            // Visualisierung der Attack-Hitbox
            if (_attackTimer > (AttackCooldown - 0.1f))
            {
                Rectangle attackRect = new Rectangle(
                    (int)Position.X + Size,
                    (int)Position.Y + Size / 4,
                    (int)AttackRange,
                    Size / 2
                );
                spriteBatch.Draw(pixel, attackRect, Color.OrangeRed);
            }
        }
    }
}
