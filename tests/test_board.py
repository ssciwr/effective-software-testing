from effective_software_testing.board import Board, Player
import pytest


board_sizes = [(1, 1), (2, 2), (1, 2), (2, 1), (3, 3)]
valid_players = [Player.CROSS, Player.CIRCLE]


@pytest.mark.parametrize("rows,cols", board_sizes)
def test_empty_rows_x_cols_board(rows: int, cols: int) -> None:
    board = Board(rows=rows, cols=cols)
    assert board.n_cols == cols
    assert board.n_rows == rows
    for row in range(rows):
        for col in range(cols):
            assert board.square(row, col) == Player.EMPTY


@pytest.mark.parametrize("player", valid_players)
@pytest.mark.parametrize("rows,cols", board_sizes)
def test_empty_1x1_board_make_move_valid(rows: int, cols: int, player: Player) -> None:
    for row in range(rows):
        for col in range(cols):
            board = Board(rows, cols)
            assert board.square(row, col) == Player.EMPTY
            assert board.make_move(row, col, player) is True
            assert board.square(row, col) == player


@pytest.mark.parametrize("rows,cols", board_sizes)
def test_empty_1x1_board_make_move_invalid_player(rows: int, cols: int) -> None:
    for row in range(rows):
        for col in range(cols):
            board = Board(rows, cols)
            assert board.square(row, col) == Player.EMPTY
            assert board.make_move(row, col, Player.CROSS) is False
            assert board.square(row, col) == Player.EMPTY


@pytest.mark.parametrize("player", valid_players)
@pytest.mark.parametrize("row,col", [(-1, -2), (6, 7), (5, 4), (4, 4)])
@pytest.mark.parametrize("rows,cols", board_sizes)
def test_empty_1x1_board_make_move_invalid_row_col(
    player: Player, rows: int, cols: int, row: int, col: int
) -> None:
    board = Board(rows, cols)
    assert board.make_move(row, col, player) is False
