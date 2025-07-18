from enum import Enum
from itertools import product
from typing import Any, Iterable, Callable
import os

from color_print import ColorPrint, Color


def game_log(func: Callable[..., str]) -> Callable[..., str]:
    """Decorator for registering game logs.

    Args:
        func (Callable[..., str]): The function to be decorated.

    Returns:
        Callable[..., str]: The decorated function.
    """

    def wrapper(*args: Any, **kwargs: Any) -> str:
        result: str = func(*args, **kwargs)
        with open("game_log.txt", "a") as log_file:
            log_file.write(f"{result}\n")
        return result

    return wrapper


class MOVE(Enum):
    RIGHT = "right"
    LEFT = "left"
    UP = "up"
    DOWN = "down"


DIRECTIONS: dict[MOVE, tuple[int, int, int, int]] = {
    MOVE.RIGHT: (0, 2, 0, 1),
    MOVE.LEFT: (0, -2, 0, -1),
    MOVE.UP: (-2, 0, -1, 0),
    MOVE.DOWN: (2, 0, 1, 0),
}
ALPHABET: str = "ABCDEFG"


class Solitaire:
    """Represents a game of Solitaire.
    Attributes:
        size (int): The size of the board.
        corner_size (tuple[int, int]): The size of the corners.
        board (list[list[str]]): The game board.
        counter (Callable[[], int]): A function to count the number of moves made.

    Args:
        size (int): The size of the board. Default is 7.
        corner_size (tuple[int, int]): The size of the corners. Default is (2, 2).
    """

    def __init__(self, size: int = 7) -> None:
        self._size: int = size
        self._corner_size: tuple[int, int] = (2, 2)
        self.board: list[list[str]] = self._setup_board()
        self.counter: Callable[[], int] = self._create_counter()

    def _setup_board(self) -> list[list[str]]:
        """Set up the initial game board.

        Returns:
            list[list[str]]: The initial game board.
        """

        def is_corner(row: int, col: int) -> bool:
            """Check if the given cell is in one of the four corners of the board.

            Args:
                row (int): The row index of the cell.
                col (int): The column index of the cell.

            Returns:
                bool: True if the cell is in a corner, False otherwise.
            """
            rows_in_corner: bool = (
                row < self._corner_size[0] or row >= self._size - self._corner_size[0]
            )
            cols_in_corner: bool = (
                col < self._corner_size[1] or col >= self._size - self._corner_size[1]
            )
            return rows_in_corner and cols_in_corner

        self.board = [
            [" " if is_corner(row=row, col=col) else "1" for col in range(self._size)]
            for row in range(self._size)
        ]

        center: int = self._size // 2

        self.board[center][center] = "0"

        return self.board

    def show_board(self) -> None:

        print("  ", end="")
        for i in range(self._size):
            ColorPrint.print_colored(str(i + 1), Color.BLUE, end=" ")
        print()
        for row, cells in enumerate(self.board):
            # print(alphabet[row], end="|")
            # for cell in cells:
            #     print(cell, end="|")
            # print()
            ColorPrint.print_colored(ALPHABET[row], Color.BLUE, end="|")
            for cell in cells:
                color = Color.RED if cell == "1" else Color.GREEN
                ColorPrint.print_colored(cell, color, end="|")
            print()

    def get_valid_moves(self) -> list[tuple[int, int, MOVE]]:
        def is_valid_move(row: int, col: int, direction: MOVE) -> bool:
            """Check if a move is valid.

            Args:
                row (int): The row index of the peg.
                col (int): The column index of the peg.
                direction (MOVE): The direction of the move.

            Returns:
                bool: True if the move is valid, False otherwise.
            """

            if direction not in DIRECTIONS:
                return False

            row_offset, col_offset, remove_row_offset, remove_col_offset = DIRECTIONS[
                direction
            ]

            row_moved: int = row + row_offset
            col_moved: int = col + col_offset
            removed_row: int = row + remove_row_offset
            removed_col: int = col + remove_col_offset

            return (
                0 <= row_moved < self._size
                and 0 <= col_moved < self._size
                and self.board[row][col] == "1"
                and self.board[row_moved][col_moved] == "0"
                and self.board[removed_row][removed_col] == "1"
            )

        all_options: Iterable[tuple[int, int, MOVE]] = product(
            range(self._size), range(self._size), DIRECTIONS.keys()
        )

        return list(
            filter(
                lambda option: is_valid_move(option[0], option[1], option[2]),
                all_options,
            )
        )

    def show_moves(self, moves: list[tuple[int, int, MOVE]]) -> None:
        """Display the valid moves on the board.

        Args:
            moves (list[tuple[int, int, MOVE]]): The list of valid moves.
        """
        mapped_moves: list[tuple[str, int, str]] = list(
            map(lambda move: (ALPHABET[move[0]], move[1] + 1, move[2].value), moves)
        )

        for i, move in enumerate(mapped_moves):
            print(f"{i + 1} {move}")

    def apply_move(self, move: tuple[int, int, MOVE]) -> None:
        """Apply a move to the board.

        Args:
            move (tuple[int, int, MOVE]): The move to apply.
        """
        if move not in self.get_valid_moves():
            raise ValueError("Invalid move")

        row: int
        col: int
        direction: MOVE
        row, col, direction = move

        row_offset: int
        col_offset: int
        row_jump_offset: int
        col_jump_offset: int
        row_offset, col_offset, row_jump_offset, col_jump_offset = DIRECTIONS[direction]

        # Remove the peg at the starting position
        self.board[row][col] = "0"
        # Remove the peg at the position jumped over
        self.board[row + row_jump_offset][col + col_jump_offset] = "0"
        # Place the peg at the new position
        self.board[row + row_offset][col + col_offset] = "1"

    def get_selection(
        self, moves: list[tuple[int, int, MOVE]], use_random_mode: bool
    ) -> tuple[int, int, MOVE]:
        """Get a move selection from the user.

        Args:
            moves (list[tuple[int, int, MOVE]]): The list of valid moves.
            use_random_mode (bool): Whether to use random mode for selection.

        Returns:
            tuple[int, int, MOVE]: The selected move.
        """
        number_of_moves: int = len(moves)
        if use_random_mode:
            import random

            selected_move: tuple[int, int, MOVE] = random.choice(moves)
            return selected_move

        while True:
            selection: str = input(
                f"Select a move from 1 to {number_of_moves}: "
            ).strip()
            if selection.isdigit() and 1 <= int(selection) <= number_of_moves:
                return moves[int(selection) - 1]
            print("Invalid selection. Please try again.")

    def count_pegs(self) -> int:
        """Count the number of pegs on the board.

        Returns:
            int: The number of pegs on the board.
        """
        return sum(row.count("1") for row in self.board)

    def validate_win(self) -> bool:
        """Check if the game is won.

        Returns:
            bool: True if the game is won, False otherwise.
        """
        return (
            self.count_pegs() == 1
            and self.board[self._size // 2][self._size // 2] == "1"
        )

    def _create_counter(self) -> Callable[[], int]:
        """Create a counter for the number of moves made.

        Returns:
            Callable[None, int]: A function that returns the number of moves made.
        """
        count: int = 0

        def increase() -> int:
            nonlocal count
            count += 1
            return count

        return increase

    @game_log
    def end_game(self) -> str:
        """End the game and display the result."""
        moves_made: int = self.counter() - 1
        remaining_pegs: int = self.count_pegs()
        return f"{'VICTORY' if self.validate_win() else 'DEFEAT'} | Moves made: {moves_made} | Remaining pegs: {remaining_pegs}"


def ask_random_mode() -> bool:
    """Ask the user if they want to play in random mode.

    Returns:
        bool: True if the user wants to play in random mode, False otherwise.
    """
    while True:
        choice: str = (
            input("Do you want to play in random mode? (y/n): ").strip().lower()
        )
        if choice in ("y", "n"):
            return choice == "y"
        print("Invalid choice. Please enter 'y' or 'n'.")


def ask_custom_size() -> int:
    """Ask the user for a custom board size."""
    while True:
        size: str = input("Enter the board size (default is 7): ").strip()
        if not size:
            return 7
        if size.isdigit() and int(size) % 2 == 1:
            return int(size)
        print("Invalid size. Please enter an odd number.")


def main() -> None:
    os.system("cls" if os.name == "nt" else "clear")

    print("Welcome to Peg Solitaire!")

    size: int = ask_custom_size()

    use_random_mode: bool = ask_random_mode()
    os.system("cls" if os.name == "nt" else "clear")

    game: Solitaire = Solitaire(size=size)

    is_playing: bool = True
    while is_playing:
        game.show_board()
        moves: list[tuple[int, int, MOVE]] = game.get_valid_moves()
        if not moves:
            print("No valid moves available. Game over!")
            is_playing = False
            continue

        game.show_moves(moves)
        selected_move: tuple[int, int, MOVE] = game.get_selection(
            moves, use_random_mode
        )

        try:
            game.apply_move(selected_move)
            game.counter()
            os.system("cls" if os.name == "nt" else "clear")
        except ValueError as e:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Error applying move: {e}")

    print(game.end_game())


main()
