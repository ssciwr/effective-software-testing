from effective_software_testing.player import Player
from effective_software_testing.board import Board
from effective_software_testing.engine import Engine
from typing import Optional
import pytest

board_sizes = [(1, 1), (2, 2), (3, 3), (1, 2), (3, 1)]
valid_players = [Player.CROSS, Player.CIRCLE]


def _count_squares(board: Board, player: Optional[Player]) -> int:
    count = 0
    for row in range(board.n_rows):
        for col in range(board.n_cols):
            if board.square(row, col) == player:
                count += 1
    return count


@pytest.mark.parametrize("player", valid_players)
def test_single_engine_fill_1x1_board(player: Player) -> None:
    board = Board(1, 1)
    engine = Engine(player, board)
    assert board.square(0, 0) is None
    assert engine.make_move() is True
    assert board.square(0, 0) == player
    assert engine.make_move() is False


@pytest.mark.parametrize("player", valid_players)
def test_single_engine_fill_3x3_board(player: Player) -> None:
    board = Board(3, 3)
    engine = Engine(player, board)
    assert _count_squares(board, player) == 0
    num_successful_moves = 0
    while engine.make_move():
        num_successful_moves += 1
        assert _count_squares(board, player) == num_successful_moves
        print(board)
    assert num_successful_moves == board.n_cols * board.n_cols
    assert _count_squares(board, None) == 0
    assert engine.make_move() is False


def test_two_engines_alternate_fill_3x3_board() -> None:
    board = Board(3, 3)
    engine_cross = Engine(Player.CROSS, board)
    engine_circle = Engine(Player.CIRCLE, board)
    assert _count_squares(board, Player.CROSS) == 0
    assert _count_squares(board, Player.CIRCLE) == 0
    num_cross = 0
    num_circle = 0
    while num_circle + num_cross < board.n_cols * board.n_rows:
        if engine_cross.make_move():
            num_cross += 1
        if engine_circle.make_move():
            num_circle += 1
        assert _count_squares(board, Player.CROSS) == num_cross
        assert _count_squares(board, Player.CIRCLE) == num_circle
        assert num_cross >= num_circle
    assert _count_squares(board, None) == 0
    assert engine_cross.make_move() is False
    assert engine_circle.make_move() is False
