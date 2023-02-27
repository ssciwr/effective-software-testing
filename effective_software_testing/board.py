from effective_software_testing.player import Player
from typing import Optional

# todo: implement a Board


class Board:
    def __init__(self) -> None:
        self.n = 3
        self.squares = [[None for _ in range(self.n)] for _ in range(self.n)]

    def get_square(self, row: int, col: int) -> Optional[Player]:
        return self.squares[col][row]
