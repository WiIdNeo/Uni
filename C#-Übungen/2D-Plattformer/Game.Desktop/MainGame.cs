using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;

namespace Game.Desktop
{
    public class MainGame : Game
    {
        private GraphicsDeviceManager _graphics;
        private SpriteBatch _spriteBatch;
        private Texture2D _pixel;

        private TileMap _tileMap;
        private Camera _camera;

        private List<Entity> _entities;

        public MainGame()
        {
            _graphics = new GraphicsDeviceManager(this);
            Content.RootDirectory = "Content";
            IsMouseVisible = true;
        }

        protected override void LoadContent()
        {
            _spriteBatch = new SpriteBatch(GraphicsDevice);

            _pixel = new Texture2D(GraphicsDevice, 1, 1);
            _pixel.SetData(new[] { Color.White });

            var json = File.ReadAllText("level01.json");
            var levelData = JsonSerializer.Deserialize<LevelData>(json);
            _tileMap = new TileMap(levelData);

            _camera = new Camera(_graphics.PreferredBackBufferWidth,
                                 _graphics.PreferredBackBufferHeight);

            _entities = new List<Entity>();

            // Player hinzufügen
            var player = new Player(new Vector2(2 * _tileMap.TileSize, 2 * _tileMap.TileSize), _tileMap.TileSize);
            _entities.Add(player);
        }

        protected override void Update(GameTime gameTime)
        {
            if (Keyboard.GetState().IsKeyDown(Keys.Escape))
                Exit();

            float dt = (float)gameTime.ElapsedGameTime.TotalSeconds;

            // --- Step 1: Input/KI für alle Entities ---
            foreach (var entity in _entities)
                entity.Update(gameTime, _tileMap);

            // --- Step 2: Physics zentral für alle Entities ---
            UpdatePhysics(dt);

            // --- Kamera folgt Player ---
            _camera.Follow(_entities[0].Position,
                           _tileMap.Width * _tileMap.TileSize,
                           _tileMap.Height * _tileMap.TileSize);

            base.Update(gameTime);
        }

        // --- Step 3: Physics-Methode (zentral) ---
        private void UpdatePhysics(float dt)
        {
            foreach (var entity in _entities)
            {
                // --- Gravity ---
                if (!entity.OnGround)
                {
                    float gravity = entity is Player pl ? pl.Gravity : 1000f;
                    float fallMultiplier = entity is Player pl2 ? pl2.FallMultiplier : 1f;
                    float lowJumpMultiplier = entity is Player pl3 ? pl3.LowJumpMultiplier : 1f;

                    if (entity.Velocity.Y > 0) // fallend
                        entity.Velocity.Y += gravity * (fallMultiplier - 1f) * dt;
                    else if (entity.Velocity.Y < 0) // aufsteigend
                        entity.Velocity.Y += gravity * (lowJumpMultiplier - 1f) * dt;

                    entity.Velocity.Y += gravity * dt;
                }

                // Max Fall Speed
                float maxFall = entity is Player pl4 ? pl4.MaxFallSpeed : 600f;
                if (entity.Velocity.Y > maxFall) entity.Velocity.Y = maxFall;

                // --- Position Update & Kollision ---
                Vector2 newPos = entity.Position + entity.Velocity * dt;

                if (CheckCollisionWithTiles(entity, newPos))
                {
                    // Horizontal
                    while (!CheckCollisionWithTiles(entity, new Vector2(newPos.X - Math.Sign(entity.Velocity.X), entity.Position.Y)))
                        newPos.X -= Math.Sign(entity.Velocity.X);
                    entity.Velocity.X = 0;

                    // Vertikal
                    while (!CheckCollisionWithTiles(entity, new Vector2(newPos.X, newPos.Y - Math.Sign(entity.Velocity.Y))))
                        newPos.Y -= Math.Sign(entity.Velocity.Y);

                    if (entity.Velocity.Y > 0) entity.OnGround = true;
                    entity.Velocity.Y = 0;
                }
                else
                {
                    entity.OnGround = false;
                }

                entity.Position = newPos;
                entity.IsFalling = entity.Velocity.Y > 0;
            }
        }

        protected override void Draw(GameTime gameTime)
        {
            GraphicsDevice.Clear(Color.Black);

            _spriteBatch.Begin(samplerState: SamplerState.PointClamp,
                               transformMatrix: _camera.GetViewMatrix());

            // --- Layer 0: Tiles ---
            _tileMap.Draw(_spriteBatch, _pixel);

            // --- Layer 1: Entities ---
            foreach (var entity in _entities)
                entity.Draw(_spriteBatch, _pixel);

            // --- Layer 2: Projektile / Partikel / Effekte ---
            //_particleSystem?.Draw(_spriteBatch); // später

            // --- Layer 3: UI ---
            //_uiManager?.Draw(_spriteBatch); // später (HP/Mana etc.)

            _spriteBatch.End();

            base.Draw(gameTime);
        }

        // Dummy-Methode für Tile-Kollision (muss du definieren)
        private bool CheckCollisionWithTiles(Entity entity, Vector2 newPos)
        {
            // Hier die Kollision mit _tileMap prüfen
            // Rückgabe true = Kollision, false = frei
            return false;
        }
    }
}
