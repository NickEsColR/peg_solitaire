# Peg Solitaire Game

A Python implementation of the classic Peg Solitaire game with colorful terminal interface and advanced features.

## About

This project was developed as part of an activity from the **Python Pro** course by **Eduardo Rios** on [Udemy](https://www.udemy.com/course/python-pro-eduardo-rios). The game demonstrates advanced Python programming concepts including object-oriented programming, decorators, enums, type hints, and functional programming techniques.

## Features

### Core Game Features

- **Interactive Terminal Interface**: Play directly in your terminal with colored output
- **Customizable Board Size**: Choose any odd-numbered board size (default: 7x7)
- **Move Validation**: Automatic validation of legal moves according to Peg Solitaire rules
- **Win Condition Detection**: Automatically detects when the game is won (one peg remaining in center)
- **Move Counter**: Tracks the number of moves made during the game
- **Game Logging**: All game results are automatically logged to `game_log.txt`

### Game Modes

- **Manual Mode**: Select moves interactively from a numbered list
- **Random Mode**: Let the computer make random valid moves automatically

### Visual Features

- **Colored Terminal Output**:
  - Blue: Board coordinates and labels
  - Red: Pegs (filled positions)
  - Green: Empty positions
- **Clear Board Display**: Grid-based board with row/column labels
- **Move List Display**: Numbered list of all valid moves in human-readable format

### Technical Features

- **Type Hints**: Full type annotation throughout the codebase
- **Enum Usage**: Structured move directions and color definitions
- **Decorator Pattern**: Game logging implemented as a decorator
- **Functional Programming**: Extensive use of `itertools`, `map`, `filter`, and lambda functions
- **Error Handling**: Robust input validation and error messages
- **Cross-Platform**: Works on Windows, macOS, and Linux

## How to Play

### Game Rules

1. The board starts with pegs in all positions except the center
2. To make a move, select a peg that can jump over an adjacent peg into an empty space
3. The jumped peg is removed from the board
4. The goal is to end with only one peg remaining in the center position

### Running the Game

```bash
python main.py
```

### Game Flow

1. Choose your board size (odd numbers only, default: 7)
2. Select game mode (manual or random)
3. Make moves by selecting from the numbered list of valid moves
4. Continue until no moves are available
5. Win by having exactly one peg in the center position

## Code Structure

### Main Components

#### `Solitaire` Class

The main game class that handles:

- Board initialization and setup
- Move validation and application
- Game state management
- Win condition checking
- Move counting

#### `ColorPrint` Class (`color_print.py`)

Utility class for colored terminal output:

- `Color` enum with BLUE, RED, and GREEN color codes
- `print_colored()` static method for printing colored text
- ANSI color code support for cross-platform compatibility

#### Key Methods

- `_setup_board()`: Creates the initial game board with proper corner handling
- `get_valid_moves()`: Finds all legal moves using itertools and filtering
- `apply_move()`: Executes a move and updates the board state
- `show_board()`: Displays the current board with colors
- `show_moves()`: Lists all valid moves in human-readable format

### Advanced Python Concepts Demonstrated

1. **Decorators**: `@game_log` decorator for automatic game logging
2. **Enums**: `MOVE` enum for move directions, `Color` enum for terminal colors
3. **Type Hints**: Complete type annotation for better code documentation
4. **Functional Programming**: Extensive use of `itertools.product`, `map`, `filter`
5. **Closures**: Counter implementation using nested functions
6. **Error Handling**: Input validation and move validation
7. **File I/O**: Game logging to external file

## Game Logging

All game results are automatically logged to `game_log.txt` with the following format:

```text
VICTORY | Moves made: 15 | Remaining pegs: 1
DEFEAT | Moves made: 23 | Remaining pegs: 5
```

## Requirements

- Python 3.7+
- No external dependencies required (uses only standard library)

## Files

- `main.py`: Main game implementation
- `color_print.py`: Colored terminal output utilities
- `README.md`: This documentation file
- `game_log.txt`: Auto-generated game log file

## Educational Value

This project demonstrates:

- Object-oriented design principles
- Functional programming techniques
- Advanced Python features (decorators, enums, type hints)
- Game logic implementation
- User interface design for terminal applications
- File handling and logging
- Cross-platform compatibility considerations

---

*This project was created as part of the Python Pro course by Eduardo Rios on Udemy. It serves as an excellent example of intermediate to advanced Python programming techniques applied to game development.*
