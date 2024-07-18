from effective_software_testing.board import Board
from effective_software_testing.player import Player
import pytest


@pytest.mark.parametrize("col", [0, 1, 2])
@pytest.mark.parametrize("row", [0, 1, 2])
def test_empty_board(row: int, col: int, tmp_path):
    board = Board()
    assert board.squares is not None
    assert len(board.squares) == 3
    assert len(board.squares[row]) == 3
    assert board.squares[row][col] is None


@pytest.mark.parametrize("player", [Player.CROSS, Player.CIRCLE])
@pytest.mark.parametrize("col", [0, 1, 2])
@pytest.mark.parametrize("row", [0, 1, 2])
def test_empty_board_make_valid_move(row, col, player):
    board = Board()
    assert board.fill_square(player, row, col)


@pytest.mark.parametrize("row,col", [(6,9), (-1,-1)])
@pytest.mark.parametrize("player", [Player.CROSS, Player.CIRCLE])
def test_empty_board_make_invalid_move(player, row, col):
    board = Board()
    with pytest.raises(IndexError):
        assert board.fill_square(player, row, col)


def test_invalid_repeat_move():
    board = Board()
    board.fill_square(Player.CROSS, 1, 1)
    assert not board.fill_square(Player.CIRCLE, 1, 1)


@pytest.mark.parametrize("squares", [((0,0), (0,1), (0,2)), ((0,0), (1,1), (2,2)), ((0,0), (1,0), (2,0))])
@pytest.mark.parametrize("player", [Player.CROSS, Player.CIRCLE])
def test_win_state(player, squares):
    board = Board()
    for square in squares:
        assert board.fill_square(player, square[0], square[1])
    assert board.winner() is player


def test_same_player_moves_twice():
    board = Board()
    board.fill_square(Player.CROSS, 0, 0)
    assert not board.fill_square(Player.CROSS, 1, 0)
