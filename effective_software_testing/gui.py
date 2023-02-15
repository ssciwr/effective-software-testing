from __future__ import annotations
from effective_software_testing.player import Player
from effective_software_testing.board import Board
from effective_software_testing.engine import Engine
from effective_software_testing.board_widget import BoardWidget
from PyQt6.QtWidgets import QMainWindow


class Gui(QMainWindow):
    def __init__(self, n: int):
        super().__init__()
        self.setWindowTitle("tic-tac-toe [Effective Software Testing]")
        self.board = Board(n)
        self.engine = Engine(Player.CROSS, self.board)
        self.board_widget = BoardWidget(self.board)
        self.setCentralWidget(self.board_widget)
        self.board_widget.square_clicked.connect(self._make_user_move)

    def _make_user_move(self, row: int, col: int) -> None:
        self.board.make_move(row, col, Player.CIRCLE)
        self.board_widget.update_image()
        self.engine.make_move()
        self.board_widget.update_image()
