from effective_software_testing.player import Player

class Board:
    def __init__(self):
        self.squares = [[None, None, None], [None, None, None], [None, None, None]]
        self.last_player = None

    def fill_square(self, player, row, col) -> bool:
        if self.last_player == player:
            return False
        if row < 0 or col < 0:
            raise IndexError("Invalid row or column: negative values not allowed")
        if self.squares[row][col] is None:
            self.squares[row][col] = player
            return True
        return False

    def winner(self) -> Player | None:
        for row in self.squares:
            if row[0] == row[1] == row[2]:
                return row[0]
        for col in range(3):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col]:
                return self.squares[0][col]
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2]:
            return self.squares[0][0]
        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0]:
            return self.squares[0][2]
        return None