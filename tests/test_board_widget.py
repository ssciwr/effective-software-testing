from effective_software_testing.board import Board
from effective_software_testing.board_widget import BoardWidget
from PyQt6.QtCore import QSize
from PyQt6.QtGui import qRgb
from PyQt6.QtWidgets import QApplication


def test_empty_board_widget() -> None:
    app = QApplication([])
    board = Board(3)
    board_widget = BoardWidget(board)
    board_widget.show()
    widget_size = QSize(103, 87)
    board_widget.resize(widget_size)
    image = board_widget.pixmap().toImage()
    assert image.size() == widget_size
    assert image.pixel(3, 3) == qRgb(0, 0, 0)
