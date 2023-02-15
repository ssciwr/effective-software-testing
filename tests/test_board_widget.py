from effective_software_testing.board import Board
from effective_software_testing.board_widget import BoardWidget
from PyQt6.QtCore import QSize
from PyQt6.QtGui import qRgb
from typing import Any


def test_empty_board_widget(qtbot: Any) -> None:
    board = Board(3)
    board_widget = BoardWidget(board)
    board_widget.show()
    qtbot.addWidget(board_widget)
    widget_size = QSize(103, 87)
    board_widget.resize(widget_size)
    image = board_widget.pixmap().toImage()
    assert image.size() == widget_size
    assert image.pixel(3, 3) == qRgb(0, 0, 0)
