from effective_software_testing.player import Player
from effective_software_testing.board import Board
import pytest

board_sizes = [(1, 1), (2, 2), (3, 3), (1, 2), (3, 1)]
valid_players = [player for player in Player]


@pytest.mark.parametrize("rows,cols", board_sizes)
def test_empty_board(rows: int, cols: int) -> None:
    board = Board(rows=rows, cols=cols)
    assert board.n_cols == cols
    assert board.n_rows == rows
    for row in range(rows):
        for col in range(cols):
            assert board.square(row, col) is None


@pytest.mark.parametrize("player", valid_players)
@pytest.mark.parametrize("rows,cols", board_sizes)
def test_empty_board_make_move_valid(rows: int, cols: int, player: Player) -> None:
    for row in range(rows):
        for col in range(cols):
            board = Board(rows, cols)
            assert board.square(row, col) is None
            assert board.make_move(row, col, player) is True
            assert board.square(row, col) == player


@pytest.mark.parametrize("player", valid_players)
@pytest.mark.parametrize("row,col", [(-1, -2), (6, 7), (5, 4), (4, 4)])
@pytest.mark.parametrize("rows,cols", board_sizes)
def test_empty_board_make_move_invalid_square(
    player: Player, rows: int, cols: int, row: int, col: int
) -> None:
    board = Board(rows, cols)
    assert board.make_move(row, col, player) is False


@pytest.mark.parametrize("player1", valid_players)
@pytest.mark.parametrize("player2", valid_players)
@pytest.mark.parametrize("rows,cols", board_sizes)
def test_make_move_square_already_taken(
    player1: Player, player2: Player, rows: int, cols: int
) -> None:
    for row in range(rows):
        for col in range(cols):
            board = Board(rows, cols)
            assert board.square(row, col) is None
            assert board.make_move(row, col, player1) is True
            assert board.square(row, col) == player1
            assert board.make_move(row, col, player2) is False
            assert board.square(row, col) == player1
