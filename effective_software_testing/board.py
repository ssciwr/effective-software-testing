from __future__ import annotations
from effective_software_testing.player import Player
from typing import Optional, List


def _player_as_char(player: Optional[Player]) -> str:
    if player == Player.CROSS:
        return "X"
    if player == Player.CIRCLE:
        return "O"
    return "."


class Board:
    """A `rows` x `cols` tic-tac-toe board where a `Player` can make a move"""

    def __init__(self, rows: int, cols: int):
        self.n_rows = rows
        self.n_cols = cols
        self._squares: List[List[Optional[Player]]] = [
            [None for _ in range(cols)] for _ in range(rows)
        ]

    def __repr__(self) -> str:
        return f"Board<{'|'.join([''.join([_player_as_char(player) for player in row]) for row in self._squares])}>"

    def square(self, row: int, col: int) -> Optional[Player]:
        """Returns the `Player` who has made a move in the square at position (`row`, `col`)

        If the square is empty, returns `None`
        """
        return self._squares[row][col]

    def make_move(self, row: int, col: int, player: Player) -> bool:
        """Make a move at position (`row`, `col`) for `player`

        If the move is legal, it makes the move and Returns `True`

        Otherwise it does nothing and returns `False`
        """
        if row < 0 or col < 0:
            return False
        try:
            if self._squares[row][col] is not None:
                return False
            self._squares[row][col] = player
            return True
        except IndexError:
            return False
