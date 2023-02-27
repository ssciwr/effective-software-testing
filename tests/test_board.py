from __future__ import annotations
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
    assert board.game_is_over is False


@pytest.mark.parametrize("n", board_sizes)
def test_empty_board_no_winner(n: int) -> None:
    board = Board(n)
    assert board.n == n
    assert board.game_winner is None


@pytest.mark.parametrize("player", players)
def test_1x1_board_first_move_wins(player: Player) -> None:
    board = Board(1)
    assert board.game_is_over is False
    assert board.game_winner is None
    board.make_move(0, 0, player)
    assert board.square(0, 0) == player
    assert board.game_is_over is True
    assert board.game_winner == player


@pytest.mark.parametrize("player", players)
@pytest.mark.parametrize("n", board_sizes)
def test_empty_board_make_move_valid(n: int, player: Player) -> None:
    for row, col in np.ndindex(n, n):
        board = Board(n)
        assert board.square(row, col) is None
        assert board.make_move(row, col, player) is True
        assert board.square(row, col) == player


@pytest.mark.parametrize("n", board_sizes)
def test_full_row_wins(n: int) -> None:
    for row in range(n):
        board = Board(n)
        assert board.game_is_over is False
        assert board.game_winner is None
        assert board.make_move(row, 0, Player.CROSS) is True
        for col in range(1, n):
            assert board.make_move((row + 1) % n, col, Player.CIRCLE) is True
            assert board.make_move(row, col, Player.CROSS) is True
        assert board.game_is_over is True
        assert board.game_winner == Player.CROSS
        assert len(board.winning_squares) == n
        for col in range(n):
            assert (row, col) in board.winning_squares
        # game over: circle cannot make move that is otherwise valid:
        assert board.make_move((row + 1) % n, 0, Player.CIRCLE) is False


@pytest.mark.parametrize("player", players)
@pytest.mark.parametrize("n", board_sizes)
def test_full_col_wins(n: int, player: Player) -> None:
    for col in range(n):
        board = Board(n)
        assert board.game_is_over is False
        assert board.game_winner is None
        assert board.make_move(0, col, Player.CROSS) is True
        for row in range(1, n):
            assert board.make_move(row, (col + 1) % n, Player.CIRCLE) is True
            assert board.make_move(row, col, Player.CROSS) is True
        assert board.game_is_over is True
        assert board.game_winner == Player.CROSS
        assert len(board.winning_squares) == n
        for row in range(n):
            assert (row, col) in board.winning_squares
        # game over: circle cannot make move that is otherwise valid:
        assert board.make_move(0, (col + 1) % n, Player.CIRCLE) is False


def test_full_diag_top_left_3x3_wins() -> None:
    board = Board(3)
    assert board.game_is_over is False
    assert board.game_winner is None
    assert board.make_move(0, 0, Player.CROSS) is True
    assert board.make_move(0, 1, Player.CIRCLE) is True
    assert board.make_move(1, 1, Player.CROSS) is True
    assert board.make_move(0, 2, Player.CIRCLE) is True
    assert board.make_move(2, 2, Player.CROSS) is True
    assert board.game_is_over is True
    assert board.game_winner == Player.CROSS
    assert len(board.winning_squares) == 3
    assert (0, 0) in board.winning_squares
    assert (1, 1) in board.winning_squares
    assert (2, 2) in board.winning_squares
    assert board.make_move(1, 2, Player.CIRCLE) is False


def test_full_diag_bottom_left_3x3_wins() -> None:
    board = Board(3)
    assert board.game_is_over is False
    assert board.game_winner is None
    assert board.make_move(0, 2, Player.CROSS) is True
    assert board.make_move(0, 1, Player.CIRCLE) is True
    assert board.make_move(1, 1, Player.CROSS) is True
    assert board.make_move(1, 0, Player.CIRCLE) is True
    assert board.make_move(2, 0, Player.CROSS) is True
    assert board.game_is_over is True
    assert board.game_winner == Player.CROSS
    assert len(board.winning_squares) == 3
    assert (0, 2) in board.winning_squares
    assert (1, 1) in board.winning_squares
    assert (2, 0) in board.winning_squares
    assert board.make_move(1, 2, Player.CIRCLE) is False


@pytest.mark.parametrize("player", players)
@pytest.mark.parametrize("row,col", [(-1, -2), (6, 7), (51, 24), (8, 7)])
@pytest.mark.parametrize("n", board_sizes)
def test_empty_board_make_move_invalid_square(
    player: Player, n: int, row: int, col: int
) -> None:
    board = Board(n)
    assert board.make_move(row, col, player) is False


@pytest.mark.parametrize("player", players)
@pytest.mark.parametrize("n", board_sizes)
def test_empty_board_same_player_moves_twice(player: Player, n: int) -> None:
    board = Board(n)
    assert board.make_move(0, 0, player) is True
    assert board.make_move(0, 0, player) is False


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


def test_3x3_board_repr() -> None:
    board = Board(3)
    assert board.__repr__() == "Board<...|...|...>"
    board.make_move(0, 0, Player.CROSS)
    assert board.__repr__() == "Board<X..|...|...>"
    board.make_move(0, 2, Player.CIRCLE)
    assert board.__repr__() == "Board<X.O|...|...>"
    board.make_move(2, 2, Player.CROSS)
    assert board.__repr__() == "Board<X.O|...|..X>"
    board.make_move(1, 1, Player.CIRCLE)
    assert board.__repr__() == "Board<X.O|.O.|..X>"
