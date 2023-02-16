from __future__ import annotations
from effective_software_testing.player import Player
from effective_software_testing.board import Board
from effective_software_testing.engine import Engine
from effective_software_testing.board_widget import BoardWidget
from PyQt6.QtWidgets import QMainWindow, QMessageBox


class Gui(QMainWindow):
    def __init__(self, n: int):
        super().__init__()
        self.resize(800, 800)
        self.board = Board(n)
        self.engine = Engine(Player.CROSS, self.board)
        self.board_widget = BoardWidget(self.board)
        self.board_widget.square_clicked.connect(self._make_user_move)
        self.setWindowTitle("tic-tac-toe [Effective Software Testing]")
        self.setCentralWidget(self.board_widget)

    def _make_user_move(self, row: int, col: int) -> None:
        if not self.board.make_move(row, col, Player.CIRCLE):
            # if user move was not valid, ignore it
            return
        self.board_widget.update_image()
        # make engine move
        self.engine.make_move()
        self.board_widget.update_image()
        if self.board.game_is_over:
            if self.board.game_winner == Player.CIRCLE:
                QMessageBox.information(self, "You win!", "You won the game!")
            elif self.board.game_winner == Player.CROSS:
                QMessageBox.information(self, "You lose", "You lost the game.")
            else:
                QMessageBox.information(self, "Draw", "Game ended in a draw.")
            self.close()
