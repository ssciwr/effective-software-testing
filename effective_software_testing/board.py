from __future__ import annotations
from effective_software_testing.player import Player
from typing import Optional, List, Tuple


def _player_as_char(player: Optional[Player]) -> str:
    if player == Player.CROSS:
        return "X"
    if player == Player.CIRCLE:
        return "O"
    return "."


def _get_winner(
    board: Board,
) -> Tuple[Optional[Player], Optional[List[Tuple[int, int]]]]:
    """If a player has won the game, return that `Player`, otherwise returns `None`

    Also return a list of (`row`,`col`) pairs for the squares in the winning line
    """
    # check rows and cols
    for i in range(board.n):
        for player in Player:
            if all(board.square(i, j) == player for j in range(board.n)):
                return player, [(i, j) for j in range(board.n)]
            if all(board.square(j, i) == player for j in range(board.n)):
                return player, [(j, i) for j in range(board.n)]
    # check diagonals
    for player in Player:
        if all(board.square(i, i) == player for i in range(board.n)):
            return player, [(i, i) for i in range(board.n)]
        if all(board.square(i, board.n - 1 - i) == player for i in range(board.n)):
            return player, [(i, board.n - 1 - i) for i in range(board.n)]
    # no winner
    return None, None


class Board:
    """A `n` x `n` tic-tac-toe board where a `Player` can make a move"""

    def __init__(self, n: int):
        self.n = n
        self.game_winner: Optional[Player] = None
        self.winning_squares: Optional[List[Tuple[int, int]]] = None
        self.game_is_over = False
        self._last_player: Optional[Player] = None
        self._squares: List[List[Optional[Player]]] = [
            [None for _ in range(n)] for _ in range(n)
        ]

    def __repr__(self) -> str:
        return f"Board<{'|'.join([''.join([_player_as_char(player) for player in row]) for row in self._squares])}>"

    def _update_game_state(self) -> None:
        self.game_winner, self.winning_squares = _get_winner(self)
        self.game_is_over = self.game_winner is not None or not any(
            None in row for row in self._squares
        )

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
        if row < 0 or col < 0 or self.game_is_over or player == self._last_player:
            return False
        try:
            if self._squares[row][col] is not None:
                return False
            self._squares[row][col] = player
            self._last_player = player
            self._update_game_state()
            return True
        except IndexError:
            return False
