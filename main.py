from enum import Enum


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


class Solitaire:
    def __init__(self) -> None:
        self._size: int = 7
        self._corner_size: tuple[int, int] = (2, 2)
        self.board: list[list[str]] = self._setup_board()

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
        alphabet: str = "ABCDEFGH"
        print("  ", end="")
        for i in range(self._size):
            print(i + 1, end=" ")
        print()
        for row, cells in enumerate(self.board):
            # print(alphabet[row], end="|")
            # for cell in cells:
            #     print(cell, end="|")
            # print()
            print(f"{alphabet[row]}|{'|'.join(cells)}|")


solitaire: Solitaire = Solitaire()
solitaire.show_board()
