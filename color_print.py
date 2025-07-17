from enum import Enum


class Color(Enum):
    BLUE = "\033[94m"
    RED = "\033[91m"
    GREEN = "\033[92m"


class ColorPrint:
    @staticmethod
    def print_colored(text: str, color: Color, end: str = "\n") -> None:
        print(f"{color.value}{text}\033[0m", end=end)
