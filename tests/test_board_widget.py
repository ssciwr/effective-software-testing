from effective_software_testing.board import Board
from effective_software_testing.board_widget import BoardWidget
from PyQt6.QtCore import QSize, Qt, QPoint
from pytestqt.qtbot import QtBot
import numpy as np


def _row_col_to_qpoint(row: int, col: int, n: int, image_size: QSize) -> QPoint:
    """
    Converts a `row`,`col` pair for a board with `n`x`n` squares to a point
    in the center of this square on an image of the board with size `image_size`
    """
    square_width = image_size.width() / n
    square_height = image_size.height() / n
    x = int((col + 0.5) * square_width)
    y = int((row + 0.5) * square_height)
    return QPoint(x, y)


def test_empty_board_widget_resize(qtbot: QtBot) -> None:
    n = 3
    widget_size = QSize(103, 87)
    board = Board(n)
    board_widget = BoardWidget(board)
    qtbot.add_widget(board_widget)
    with qtbot.wait_exposed(board_widget):
        board_widget.show()
    board_widget.resize(widget_size)

    def check_image() -> None:
        image = board_widget.pixmap().toImage()
        assert image.size() == widget_size
        for row, col in np.ndindex(n, n):
            point = _row_col_to_qpoint(row, col, n, widget_size)
            assert image.pixel(point) == board_widget.background_color

    qtbot.wait_until(check_image)


def test_empty_board_mouse_click_on_square(qtbot: QtBot) -> None:
    n = 3
    widget_size = QSize(123, 163)
    board = Board(n)
    board_widget = BoardWidget(board)
    qtbot.addWidget(board_widget)
    with qtbot.wait_exposed(board_widget):
        board_widget.show()
    board_widget.resize(widget_size)
    qtbot.wait_until(lambda: board_widget.size() == widget_size)
    for row, col in np.ndindex(n, n):
        point = _row_col_to_qpoint(row, col, n, widget_size)
        with qtbot.wait_signal(board_widget.square_clicked) as blocker:
            qtbot.mouseClick(board_widget, Qt.MouseButton.LeftButton, pos=point)
            assert blocker.args == [row, col]
