from effective_software_testing.player import Player
from effective_software_testing.board import Board
import pytest
import numpy as np

board_sizes = [1, 2, 3, 4, 5]
players = [player for player in Player]


@pytest.mark.parametrize("n", board_sizes)
def test_empty_board_is_empty(n: int) -> None:
    board = Board(n)
    assert board.n == n
    for row, col in np.ndindex(n, n):
        assert board.square(row, col) is None


@pytest.mark.parametrize("n", board_sizes)
def test_empty_board_game_not_over(n: int) -> None:
    board = Board(n)
    assert board.n == n
    assert board.game_over() is False


@pytest.mark.parametrize("n", board_sizes)
def test_empty_board_no_winner(n: int) -> None:
    board = Board(n)
    assert board.n == n
    assert board.winner() is None


@pytest.mark.parametrize("player", players)
@pytest.mark.parametrize("n", board_sizes)
def test_empty_board_make_move_valid(n: int, player: Player) -> None:
    for row, col in np.ndindex(n, n):
        board = Board(n)
        assert board.square(row, col) is None
        assert board.make_move(row, col, player) is True
        assert board.square(row, col) == player


@pytest.mark.parametrize("player", players)
@pytest.mark.parametrize("row,col", [(-1, -2), (6, 7), (51, 24), (8, 7)])
@pytest.mark.parametrize("n", board_sizes)
def test_empty_board_make_move_invalid_square(
    player: Player, n: int, row: int, col: int
) -> None:
    board = Board(n)
    assert board.make_move(row, col, player) is False


@pytest.mark.parametrize("player1", players)
@pytest.mark.parametrize("player2", players)
@pytest.mark.parametrize("n", board_sizes)
def test_make_move_square_already_taken(
    player1: Player, player2: Player, n: int
) -> None:
    for row, col in np.ndindex(n, n):
        board = Board(n)
        assert board.square(row, col) is None
        assert board.make_move(row, col, player1) is True
        assert board.square(row, col) == player1
        assert board.make_move(row, col, player2) is False
        assert board.square(row, col) == player1


@pytest.mark.parametrize("n", board_sizes)
def test_make_move_after_game_is_won(n: int) -> None:
    board = Board(n)
    assert board.game_over() is False
    assert board.winner() is None
    # both players try to make a row, starting with CROSS
    board.make_move(0, 0, Player.CROSS)
    for i in range(1, n):
        board.make_move(n - 1, i, Player.CIRCLE)
        board.make_move(0, i, Player.CROSS)
    # CROSS has made a row, CIRCLE has not
    assert board.game_over()
    assert board.winner() == Player.CROSS
    # CIRCLE cannot make a move
    assert board.make_move(n - 1, 0, Player.CIRCLE) is False
