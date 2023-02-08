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
    """A `n` x `n` tic-tac-toe board where a `Player` can make a move"""

    def __init__(self, n: int):
        self.n = n
        self._squares: List[List[Optional[Player]]] = [
            [None for _ in range(n)] for _ in range(n)
        ]

    def __repr__(self) -> str:
        return f"Board<{'|'.join([''.join([_player_as_char(player) for player in row]) for row in self._squares])}>"

    def square(self, row: int, col: int) -> Optional[Player]:
        """Returns the `Player` who has made a move in the square at position (`row`, `col`)

        If the square is empty, returns `None`
        """
        return self._squares[row][col]

    def winner(self) -> Optional[Player]:
        # check rows and cols
        for i in range(self.n):
            for player in Player:
                if all(self._squares[i][j] == player for j in range(self.n)) or all(
                    self._squares[j][i] == player for j in range(self.n)
                ):
                    return player
        # check diagonals
        for player in Player:
            if all(self._squares[i][i] == player for i in range(self.n)) or all(
                self._squares[i][-1 - i] == player for i in range(self.n)
            ):
                return player
        # no winner
        return None

    def game_over(self) -> bool:
        if self.winner():
            return True
        return not any(None in row for row in self._squares)

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
