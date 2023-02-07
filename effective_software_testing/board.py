from enum import Enum


class Square(Enum):
    EMPTY = 0
    CROSS = 1
    CIRCLE = 2


class Board:
    def __init__(self, rows: int, cols: int):
        self.n_rows = rows
        self.n_cols = cols
        self._squares = [[Square.EMPTY] * cols] * rows

    def square(self, row: int, col: int) -> Square:
        return self._squares[row][col]
