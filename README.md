## Platformer Mini Game 🎮

Welcome to the Platformer Mini Game! This is a simple 2D platformer mini game built using Python and Pygame. The objective of the game is to navigate through the level, avoid traps, collect cherries, and reach the end point.

### Features ✨
- Side-scrolling platformer action
- Collectible cherries 🍒
- Traps and obstacles to avoid 🔥
- Health system with heart indicators ❤️
- Win and game over screens 🎉
- Customizable backgrounds and characters 🎨

### How to Play 🎮
- **Move Left**: Press the Left Arrow key ⬅️
- **Move Right**: Press the Right Arrow key ➡️
- **Jump**: Press the Spacebar (double jump is allowed) ⬆️

### Requirements 🛠️
- Python 3.x
- Pygame

### Installation 💻
1. **Clone the Repository**
   ```sh
   git clone https://github.com/JacksonJS12/Python-Minigame.git
   cd Python-Minigame/src
   ```

2. **Install Pygame**
   ```sh
   pip install pygame
   ```

3. **Run the Game**
   ```sh
   python main.py
   ```

### Customization Options 🎨
You can change the background and the character in the game to suit your preferences.

**Background Options:**
- Blue
- Brown
- Gray
- Green
- Pink
- Purple
- Yellow

To change the background, modify the following line in `main.py`:
```python
background, bg_image = get_background("Blue.png", WIDTH, HEIGHT)
```
Replace `"Blue.png"` with any of the other available options (e.g., `"Yellow.png"`).

**Character Options:**
- MaskDude
- NinjaFrog
- PinkMan
- VirtualGuy

To change the character, modify the following line in `player.py`:
```python
self.SPRITES = load_sprite_sheets("MainCharacters", "NinjaFrog", 32, 32, True)
```
Replace `"NinjaFrog"` with any of the other available options (e.g., `"MaskDude"`).

### Game Objective 🎯
- Collect all the cherries scattered throughout the level. 🍒
- Avoid traps (fire) to prevent losing health. 🔥
- Reach the end point to win the game. 🏁

### Health System ❤️
- The player starts with 3 lives, indicated by hearts at the top right of the screen. ❤️❤️❤️
- Colliding with traps will cause the player to lose a life. 💔
- The game ends when the player loses all lives. 🛑

### Winning the Game 🏆
- Collect as many cherries as possible. 🍒
- Navigate through obstacles and traps. 🔥
- Reach the end point to win the game. A win screen will display your total cherries collected. 🎉

### Losing the Game 💀
- If the player loses all lives, a game over screen will appear. 🛑

Enjoy playing the Platformer Mini Game! Feel free to contribute and improve the game by submitting pull requests. 🚀
