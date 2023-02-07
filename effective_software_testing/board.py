from enum import Enum


class Player(Enum):
    EMPTY = 0
    CROSS = 1
    CIRCLE = 2


class Board:
    def __init__(self, rows: int, cols: int):
        self.n_rows = rows
        self.n_cols = cols
        self._squares = [[Player.EMPTY] * cols] * rows

    def square(self, row: int, col: int) -> Player:
        return self._squares[row][col]

    def make_move(self, row: int, col: int, player: Player) -> bool:
        if player == Player.EMPTY or row < 0 or col < 0:
            return False
        try:
            if self._squares[row][col] != Player.EMPTY:
                return False
            self._squares[row][col] = player
            return True
        except IndexError:
            return False
