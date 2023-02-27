from effective_software_testing.board import Board, BoardException
import pytest


def test_empty_board_valid_squares() -> None:
    board = Board()
    assert board.square(0, 0) is None
    assert board.square(2, 2) is None


def test_empty_board_invalid_squares() -> None:
    board = Board()
    with pytest.raises(BoardException):
        board.square(3, 3)
    with pytest.raises(BoardException):
        board.square(-1, -2)
