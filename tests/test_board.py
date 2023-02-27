from effective_software_testing.board import Board
import pytest


def test_empty_board_valid_squares() -> None:
    board = Board()
    assert board.get_square(0, 0) is None
    assert board.get_square(2, 2) is None


def test_empty_board_invalid_squares() -> None:
    board = Board()
    with pytest.raises(IndexError):
        board.get_square(3, 3)
