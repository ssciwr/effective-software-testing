from __future__ import annotations
from effective_software_testing.board import Board
from effective_software_testing.player import Player
import numpy as np
from typing import Optional


class Engine:
    """A simple tic-tac-toe engine that makes random moves"""

    def __init__(self, player: Player, board: Board, seed: Optional[int] = None):
        self._player = player
        self._board = board
        self._rng = np.random.default_rng(seed)
        self._indices = np.array(list(np.ndindex(board.n, board.n)))

    def make_move(self) -> bool:
        """Make a random valid move and return True.

        If no valid move is possible, return False"""
        self._rng.shuffle(self._indices)
        # try each square in a random order until a move is valid
        for row, col in self._indices:
            if self._board.make_move(row, col, self._player):
                return True
        return False
