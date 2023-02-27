from effective_software_testing.player import Player
from typing import Optional, List


class BoardException(ValueError):
    pass


class Board:
    def __init__(self) -> None:
        self.n = 3
        self.squares: List[List[Optional[Player]]] = [
            [None for _ in range(self.n)] for _ in range(self.n)
        ]

    def square(self, row: int, col: int) -> Optional[Player]:
        """If a `Player` has made a move at (`row`,`col`) returns the `Player`, otherwise returns `None`"""
        if not 0 <= row < self.n:
            raise BoardException(f"Invalid row {row}")
        if not 0 <= col < self.n:
            raise BoardException(f"Invalid col {col}")
        return self.squares[col][row]

    def make_move(self, row: int, col: int, player: Player) -> bool:
        """If possible, make move for `Player` at (`row`,`col`) and return `True`, otherwise return `False`."""
        if self.square(row, col) is None:
            self.squares[col][row] = player
            return True
        return False
