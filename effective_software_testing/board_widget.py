from __future__ import annotations
from effective_software_testing.board import Board
from effective_software_testing.player import Player
from typing import Tuple
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QSize, QPoint, pyqtSignal
from PyQt6.QtGui import QPixmap, QPainter, QColor, QPen, QMouseEvent, QResizeEvent
import numpy as np


def _pos_to_row_col(pos: QPoint, size: QSize, n: int) -> Tuple[int, int]:
    row = int(n * pos.y() / size.height())
    col = int(n * pos.x() / size.width())
    return row, col


def _board_as_pixmap(board: Board, size: QSize) -> QPixmap:
    pixmap = QPixmap(size)
    pixmap.fill(0)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    dx = int(size.width() / board.n)
    dy = int(size.height() / board.n)
    padding = 0.1
    pen_color = QColor(255, 255, 255)
    pen_width = max(2, int(0.01 * min(size.width(), size.height())))
    painter.setPen(pen_color)
    for row in range(board.n):
        painter.drawLine(0, row * dy, size.width(), row * dy)
        painter.drawLine(row * dx, 0, row * dx, size.height())
    painter.setPen(QPen(pen_color, pen_width))
    w = int(dx * (1.0 - 2.0 * padding))
    h = int(dy * (1.0 - 2.0 * padding))
    for row, col in np.ndindex(board.n, board.n):
        x0 = int((col + padding) * dx)
        y0 = int((row + padding) * dy)
        if board.square(row, col) == Player.CIRCLE:
            painter.drawEllipse(x0, y0, w, h)
        elif board.square(row, col) == Player.CROSS:
            painter.drawLine(x0, y0, x0 + w, y0 + h)
            painter.drawLine(x0, y0 + h, x0 + w, y0)
    painter.end()
    return pixmap


class BoardWidget(QLabel):
    square_clicked = pyqtSignal([int, int])

    def __init__(self, board: Board):
        super().__init__()
        self.setMinimumSize(32, 32)
        self.board = board

    def update_image(self) -> None:
        self.setPixmap(_board_as_pixmap(self.board, self.size()))

    def mousePressEvent(self, event: QMouseEvent) -> None:
        row, col = _pos_to_row_col(event.pos(), self.size(), self.board.n)
        self.square_clicked.emit(row, col)

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.update_image()
