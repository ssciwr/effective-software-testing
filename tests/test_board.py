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
    with pytest.raises(BoardException, match=r".*row.*"):
        board.make_move(-1, 0, player)


def test_empty_board_make_move_square_already_taken() -> None:
    board = Board()
    assert board.make_move(0, 0, Player.CROSS) is True
    assert board.make_move(0, 0, Player.CROSS) is False
    assert board.make_move(0, 0, Player.CIRCLE) is False


def test_make_move_game_already_over(board_2x_2o: Board) -> None:
    board = board_2x_2o
    assert board.game_over() is False
    assert board.winner() is None
    # CROSS plays winning move
    assert board.make_move(0, 2, Player.CROSS) is True
    assert board.game_over()
    assert board.winner() == Player.CROSS
    # CROSS has won, circle cannot make a move:
    assert board.make_move(1, 2, Player.CIRCLE) is False


def test_board_repr(board_2x_2o: Board) -> None:
    board = board_2x_2o
    assert board.__repr__() == "<XX-|OO-|--->"
