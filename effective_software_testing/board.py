from effective_software_testing.player import Player
from typing import Optional


class BoardException(ValueError):
    pass


class Board:
    def __init__(self) -> None:
        self.n = 3
        self.squares = [[None for _ in range(self.n)] for _ in range(self.n)]

    def square(self, row: int, col: int) -> Optional[Player]:
        if not 0 <= row < self.n:
            raise BoardException(f"Invalid row {row}")
        if not 0 <= col < self.n:
            raise BoardException(f"Invalid col {col}")
        return self.squares[col][row]
