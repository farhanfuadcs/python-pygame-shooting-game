# Shooting Game by FUAD

A 2D spaceship shooting game developed using Python and Pygame. Control a yellow spaceship, fight against a red AI-controlled opponent, dodge incoming bullets, and try to defeat your opponent before your health reaches zero.

## Game Features

- **Player movement:** Control the yellow spaceship using WASD keys.
- **AI opponent:** Fight against a red spaceship controlled by an AI.
- **AI movement:** The opponent follows the player's vertical position and attempts to dodge incoming bullets.
- **Shooting system:** Fire bullets using the left mouse button.
- **Bullet collision detection:** Detects when bullets hit either spaceship.
- **Health system:** Both spaceships start with 10 health points.
- **Sound effects:** Includes shooting and bullet impact sounds.
- **Win and lose conditions:** Displays the winner when either spaceship runs out of health.
- **Restart system:** Choose whether to play another round after the game ends.

## Technologies Used

- Python
- Pygame
- Tkinter message boxes
- Random-free AI movement logic
- Collision detection
- Event handling
- Object positioning using rectangles

## Game Controls

| Control | Action |
|---|---|
| W | Move Up |
| A | Move Left |
| S | Move Down |
| D | Move Right |
| Left Mouse Button | Shoot |

## Game Information

- Window resolution: 800 × 600
- Frame rate: 60 FPS
- Player spaceship: Yellow
- AI opponent: Red
- Starting health: 10 for each spaceship
- Maximum active bullets: 4 per spaceship

## Project Structure

```text
python-pygame-shooting-game/
│
├── game.py
├── requirements.txt
├── README.md
│
└── Assets/
    ├── space.png
    ├── Yellow spaceship.png
    ├── Red spaceship.png
    ├── shootingsound.mp3
    └── bulletimpact.mp3
```

## Installation

Make sure Python is installed on your computer.

Install Pygame:

```bash
pip install -r requirements.txt
```

## How to Run

1. Clone or download this repository.
2. Make sure the `Assets` folder and all required files are present.
3. Open a terminal in the project directory.
4. Run:

```bash
python game.py
```

## How the Game Works

1. The game creates two spaceships: a yellow player spaceship and a red AI opponent.
2. The player moves using the WASD keys.
3. The player fires bullets using the left mouse button.
4. The AI opponent tracks the player's vertical position and attempts to dodge incoming bullets.
5. Both spaceships can shoot and damage each other.
6. Each successful hit reduces the opponent's health by one point.
7. When either spaceship reaches zero health, the game announces the winner.
8. A restart prompt allows the player to start another round.


## Purpose

This project was developed to practice Python game development using Pygame, including game loops, keyboard and mouse input, AI behavior, collision detection, bullet mechanics, sound effects, and game-state management.
