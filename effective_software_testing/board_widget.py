from __future__ import annotations
from effective_software_testing.board import Board
from effective_software_testing.player import Player
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QSize, pyqtSignal
from PyQt6.QtGui import QPixmap, QPainter, QMouseEvent, QResizeEvent, qRgb
import numpy as np
from typing import Optional


def _draw_board_lines(painter: QPainter, size: QSize, n: int) -> None:
    square_width = int(size.width() / n)
    square_height = int(size.height() / n)
    for row in range(n):
        painter.drawLine(0, row * square_height, size.width(), row * square_height)
        painter.drawLine(row * square_width, 0, row * square_width, size.height())


def _draw_player_shape(
    painter: QPainter,
    player: Optional[Player],
    x0: int,
    y0: int,
    shape_width: int,
    shape_height: int,
) -> None:
    if player == Player.CIRCLE:
        painter.drawEllipse(x0, y0, shape_width, shape_height)
    elif player == Player.CROSS:
        painter.drawLine(x0, y0, x0 + shape_width, y0 + shape_height)
        painter.drawLine(x0, y0 + shape_height, x0 + shape_width, y0)


def _draw_player_shapes(painter: QPainter, size: QSize, board: Board) -> None:
    fractional_pen_width = 0.02
    pen_width = max(2, int(fractional_pen_width * min(size.width(), size.height())))
    pen = painter.pen()
    pen.setWidth(pen_width)
    painter.setPen(pen)
    fractional_padding = 0.15
    shape_fractional_size = 1.0 - 2.0 * fractional_padding
    shape_width = int(shape_fractional_size * size.width() / board.n)
    shape_height = int(int(shape_fractional_size * size.height() / board.n))
    for row, col in np.ndindex(board.n, board.n):
        x0 = int((col + fractional_padding) * size.width() / board.n)
        y0 = int((row + fractional_padding) * size.height() / board.n)
        _draw_player_shape(
            painter, board.square(row, col), x0, y0, shape_width, shape_height
        )


def _board_as_pixmap(
    board: Board, size: QSize, background_color: qRgb, foreground_color: qRgb
) -> QPixmap:
    pixmap = QPixmap(size)
    pixmap.fill(background_color)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setPen(foreground_color)
    _draw_board_lines(painter, size, board.n)
    _draw_player_shapes(painter, size, board)
    painter.end()
    return pixmap


class BoardWidget(QLabel):
    square_clicked = pyqtSignal([int, int])

    def __init__(
        self,
        board: Board,
        background_color: qRgb = qRgb(0, 0, 0),
        foreground_color: qRgb = qRgb(255, 255, 255),
    ):
        super().__init__()
        self.setMinimumSize(32, 32)
        self.board = board
        self.background_color = background_color
        self.foreground_color = foreground_color

    def update_image(self) -> None:
        self.setPixmap(
            _board_as_pixmap(
                self.board, self.size(), self.background_color, self.foreground_color
            )
        )

    def mousePressEvent(self, event: QMouseEvent) -> None:
        row = int(self.board.n * event.pos().y() / self.size().height())
        col = int(self.board.n * event.pos().x() / self.size().width())
        self.square_clicked.emit(row, col)

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.update_image()
