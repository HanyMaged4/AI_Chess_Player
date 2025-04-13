# AI Chess Player

AI Chess Player is a Python-based chess game with two difficulty levels: Beginner and Advanced. It uses the `pygame` library for the graphical interface and the `python-chess` library for chess logic. The game features an AI opponent that uses the Minimax algorithm with Alpha-Beta pruning for decision-making.

## Features

- **Two Difficulty Levels**:
  - Beginner: Uses a simpler evaluation function for AI moves.
  - Advanced: Uses a more sophisticated evaluation function for AI moves.
- **Graphical Interface**:
  - Interactive chessboard with drag-and-drop functionality.
  - Visual feedback for selected pieces.
- **Sound Effects**:
  - Sounds for moves, captures, and checkmate.
- **Game Modes**:
  - Play against the AI in either difficulty level.
- **Game Over Detection**:
  - Detects checkmate, stalemate, and draw conditions.

## Requirements

- Python 3.11 or higher
- Required Python libraries:
  - `pygame`
  - `python-chess`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd AI_Chess_Player
   ```

2. Install the required libraries:
   ```bash
   pip install pygame python-chess
   ```

## How to Start

1. Run the main script:
   ```bash
   python main.py
   ```

2. Select the difficulty level on the start screen:
   - Beginner
   - Advanced

3. Play the game by dragging and dropping pieces on the board.

## Project Structure

- **`main.py`**: Entry point of the application.
- **`Game.py`**: Handles the game logic and user interactions.
- **`GameStart.py`**: Manages the start screen.
- **`GameHelper.py`**: Provides helper functions for the game.
- **`minimax.py`**: Implements the Minimax algorithm for the Beginner AI.
- **`minimax2.py`**: Implements the Minimax algorithm for the Advanced AI.
- **`evaluation.py`**: Contains evaluation functions for board states.
- **`config.py`**: Stores configuration settings like colors and board size.

## Notes

- The game uses assets like images and sounds located in the `assets` folder. Ensure the folder structure is intact for the game to run properly.
- The AI's depth is set to 3 for both difficulty levels. You can adjust this in the `Game.py` file for a harder or easier AI.
