from effective_software_testing.board import Board, BoardException
import pytest


@pytest.mark.parametrize("row", [0, 1, 2])
@pytest.mark.parametrize("col", [0, 1, 2])
def test_empty_board_valid_squares(row: int, col: int) -> None:
    board = Board()
    assert board.square(row, col) is None


def test_empty_board_invalid_squares() -> None:
    board = Board()
    with pytest.raises(BoardException) as e:
        board.square(3, 2)
    assert "row" in str(e.value)
    with pytest.raises(BoardException) as e:
        board.square(0, -2)
    assert "col" in str(e.value)
