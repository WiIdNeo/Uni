using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using System.IO;
using System.Text.Json;

namespace Game.Desktop
{
    public class MainGame : Game
    {
        private GraphicsDeviceManager _graphics;
        private SpriteBatch _spriteBatch;

        private TileMap _tileMap;
        private Texture2D _pixel;

        private Camera _camera;
        private Vector2 _playerPosition; // Vorläufig, später Player-Objekt

        public MainGame()
        {
            _graphics = new GraphicsDeviceManager(this);
            Content.RootDirectory = "Content";
            IsMouseVisible = true;

            _graphics.PreferredBackBufferWidth = 800;
            _graphics.PreferredBackBufferHeight = 450;
        }

        protected override void LoadContent()
        {
            _spriteBatch = new SpriteBatch(GraphicsDevice);

            // 1x1 Pixel für Platzhalter-Rendering
            _pixel = new Texture2D(GraphicsDevice, 1, 1);
            _pixel.SetData(new[] { Color.White });

            // Level laden
            var json = File.ReadAllText("level01.json");
            var levelData = JsonSerializer.Deserialize<LevelData>(json);
            _tileMap = new TileMap(levelData);

            // Kamera initialisieren
            _camera = new Camera(_graphics.PreferredBackBufferWidth,
                                 _graphics.PreferredBackBufferHeight);

            // Player Startposition (Pixelkoordinaten)
            _playerPosition = new Vector2(2 * _tileMap.TileSize, 2 * _tileMap.TileSize);
        }

        protected override void Update(GameTime gameTime)
        {
            if (Keyboard.GetState().IsKeyDown(Keys.Escape))
                Exit();

            // Kamera folgt Player
            _camera.Follow(_playerPosition,
                           _tileMap.Width * _tileMap.TileSize,
                           _tileMap.Height * _tileMap.TileSize);

            base.Update(gameTime);
        }

        protected override void Draw(GameTime gameTime)
        {
            GraphicsDevice.Clear(Color.Black);

            _spriteBatch.Begin(samplerState: SamplerState.PointClamp,
                               transformMatrix: _camera.GetViewMatrix());

            _tileMap.Draw(_spriteBatch, _pixel);

            // Player als rotes Quadrat rendern
            var playerRect = new Rectangle(
                (int)_playerPosition.X,
                (int)_playerPosition.Y,
                _tileMap.TileSize,
                _tileMap.TileSize
            );
            _spriteBatch.Draw(_pixel, playerRect, Color.Red);

            _spriteBatch.End();

            base.Draw(gameTime);
        }
    }
}
