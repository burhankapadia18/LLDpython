# TicTacToe - Low Level Design

A console-based implementation of the classic Tic-Tac-Toe game built with Python, following object-oriented design principles.

## System Design

### Class Diagram
```
┌───────────────┐      ┌───────────────┐      ┌────────────────┐
│ TicTacToeGame │─────>│     Board     │      │     Player     │
└───────────────┘      └───────────────┘      └────────────────┘
        │                      │                       │
        │                      │                       │
        │                      ▼                       │
        │              ┌───────────────┐               │
        └─────────────>│     Piece     │<──────────────┘
                       └───────────────┘
                          ▲         ▲
                          │         │
                 ┌────────┴──┐  ┌───┴────────┐
                 │  PieceX   │  │   PieceO   │
                 └───────────┘  └────────────┘
```

### Components

#### Game (`game.py`)
- `TicTacToeGame`: Main game controller that manages turns, checks for win conditions, and handles game flow.

#### Models
- `Board`: Represents the game board, tracks piece placement, and displays board state.
- `Player`: Represents a player with a name and assigned piece type.
- `Piece`: Abstract base class for playing pieces with a piece type.
  - `PieceX`: Implementation of the X piece.
  - `PieceO`: Implementation of the O piece.
- `PieceType`: Enum for piece types (X and O).

### Design Patterns
- **Factory Pattern**: For creating different types of pieces (X and O).
- **Strategy Pattern**: For handling different player types (could be extended for AI players).

## Code Structure

```
tictactoe/
├── main.py                  # Entry point
├── game.py                  # Game controller
└── models/                  # Data models
    ├── board.py             # Board implementation
    ├── player.py            # Player implementation
    └── playing_piece/       # Piece implementations
        ├── piece.py         # Base piece class and enum
        ├── piece_x.py       # X piece implementation
        └── piece_o.py       # O piece implementation
```

## How to Run

```bash
python main.py
```

## Gameplay

1. The game initializes with a 3x3 board and two players (X and O).
2. Players take turns entering moves in the format "row,column" (zero-indexed).
3. The board is displayed after each move.
4. The game ends when a player forms a line (row, column, or diagonal) or when the board is full (tie).

## Design Principles

- **Single Responsibility Principle**: Each class has a single responsibility.
- **Open/Closed Principle**: The design allows for extensions (e.g., different board sizes, AI players).
- **Dependency Inversion**: High-level modules depend on abstractions, not concrete implementations.

## Future Enhancements

- AI player implementation
- Graphical user interface
- Configurable board size
- Game statistics
- Network multiplayer support 