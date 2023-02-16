from effective_software_testing.player import Player
from effective_software_testing.board import Board
from effective_software_testing.engine import Engine
from typing import Optional
import pytest
import numpy as np

players = [player for player in Player]


def _count_squares(board: Board, player: Optional[Player]) -> int:
    return sum(
        1 if board.square(i, j) == player else 0
        for i, j in np.ndindex(board.n, board.n)
    )


@pytest.mark.parametrize("player", players)
def test_engine_plays_first_1x1_board(player: Player) -> None:
    board = Board(1)
    engine = Engine(player, board)
    assert board.square(0, 0) is None
    assert board.game_is_over is False
    assert board.game_winner is None
    assert engine.make_move() is True
    assert board.square(0, 0) == player
    assert board.game_is_over is True
    assert board.game_winner == player
    assert engine.make_move() is False


@pytest.mark.parametrize("n", [2, 3, 4])
def engine_plays_second_makes_valid_move(n: int) -> None:
    for row, col in np.ndindex(n, n):
        # empty board
        board = Board(n)
        engine = Engine(Player.CROSS, board)
        assert _count_squares(board, Player.CROSS) == 0
        assert _count_squares(board, Player.CIRCLE) == 0
        # circle makes a valid initial move
        board.make_move(row, col, Player.CIRCLE)
        assert _count_squares(board, Player.CROSS) == 0
        assert _count_squares(board, Player.CIRCLE) == 1
        # engine makes a valid move
        assert engine.make_move() is True
        assert _count_squares(board, Player.CROSS) == 1
        assert _count_squares(board, Player.CIRCLE) == 1
        # engine cannot play again before circle makes another move
        assert engine.make_move() is False


@pytest.mark.parametrize("n", [1, 2, 3, 4])
@pytest.mark.parametrize("rng_seed_cross", range(5))
@pytest.mark.parametrize("rng_seed_circle", range(5))
def test_two_engines_finish_game(
    n: int, rng_seed_cross: int, rng_seed_circle: int
) -> None:
    board = Board(n)
    engine_cross = Engine(Player.CROSS, board, rng_seed_cross)
    engine_circle = Engine(Player.CIRCLE, board, rng_seed_circle)
    assert _count_squares(board, Player.CROSS) == 0
    assert _count_squares(board, Player.CIRCLE) == 0
    num_cross = 0
    num_circle = 0
    while not board.game_is_over:
        if engine_cross.make_move():
            num_cross += 1
        if engine_circle.make_move():
            num_circle += 1
        assert _count_squares(board, Player.CROSS) == num_cross
        assert _count_squares(board, Player.CIRCLE) == num_circle
        assert num_cross >= num_circle
    assert board.game_is_over is True
    if board.game_winner is None:
        assert _count_squares(board, None) == 0
    else:
        assert _count_squares(board, None) >= 0
    assert engine_cross.make_move() is False
    assert engine_circle.make_move() is False
