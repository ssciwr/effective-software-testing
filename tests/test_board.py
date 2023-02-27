from effective_software_testing.board import Board, BoardException
from effective_software_testing.player import Player
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


@pytest.mark.parametrize("row", [0, 1, 2])
@pytest.mark.parametrize("col", [0, 1, 2])
@pytest.mark.parametrize("player", [p for p in Player])
def test_empty_board_make_valid_move(row: int, col: int, player: Player) -> None:
    board = Board()
    assert board.square(row, col) is None
    assert board.make_move(row, col, player) is True
    assert board.square(row, col) == player


@pytest.mark.parametrize("player", [p for p in Player])
def test_empty_board_make_move_invalid_square(player: Player) -> None:
    board = Board()
    with pytest.raises(BoardException) as e:
        board.make_move(-1, 0, player)
    assert "row" in str(e.value)


def test_empty_board_make_move_square_taken() -> None:
    board = Board()
    assert board.make_move(0, 0, Player.CROSS) is True
    assert board.make_move(0, 0, Player.CROSS) is False
    assert board.make_move(0, 0, Player.CIRCLE) is False
