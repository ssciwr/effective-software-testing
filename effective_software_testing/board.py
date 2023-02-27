from effective_software_testing.player import Player
from typing import Optional, List


class BoardException(ValueError):
    pass


def _player_as_char(player: Optional[Player]) -> str:
    if player is None:
        return "-"
    if player is Player.CROSS:
        return "X"
    if player is Player.CIRCLE:
        return "O"


def _row_as_str(players: List[Optional[Player]]) -> str:
    return "".join(_player_as_char(player) for player in players)


class Board:
    def __init__(self) -> None:
        self.n = 3
        self.squares: List[List[Optional[Player]]] = [
            [None for _ in range(self.n)] for _ in range(self.n)
        ]

    def __repr__(self) -> str:
        return "<" + "|".join(_row_as_str(row) for row in self.squares) + ">"

    def square(self, row: int, col: int) -> Optional[Player]:
        """If a `Player` has made a move at (`row`,`col`) returns the `Player`, otherwise returns `None`"""
        if not 0 <= row < self.n:
            raise BoardException(f"Invalid row {row}")
        if not 0 <= col < self.n:
            raise BoardException(f"Invalid col {col}")
        return self.squares[row][col]

    def make_move(self, row: int, col: int, player: Player) -> bool:
        """If possible, make move for `Player` at (`row`,`col`) and return `True`, otherwise return `False`."""
        if self.square(row, col) is None:
            self.squares[row][col] = player
            return True
        return False
