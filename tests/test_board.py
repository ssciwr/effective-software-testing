from effective_software_testing.board import Board, Player
import pytest


board_sizes = [(1, 1), (2, 2), (1, 2), (2, 1), (3, 3)]
valid_players = [Player.CROSS, Player.CIRCLE]
invalid_players = [Player.EMPTY]


@pytest.mark.parametrize("rows,cols", board_sizes)
def test_empty_board(rows: int, cols: int) -> None:
    board = Board(rows=rows, cols=cols)
    assert board.n_cols == cols
    assert board.n_rows == rows
    for row in range(rows):
        for col in range(cols):
            assert board.square(row, col) == Player.EMPTY


@pytest.mark.parametrize("player", valid_players)
@pytest.mark.parametrize("rows,cols", board_sizes)
def test_empty_board_make_move_valid(rows: int, cols: int, player: Player) -> None:
    for row in range(rows):
        for col in range(cols):
            board = Board(rows, cols)
            assert board.square(row, col) == Player.EMPTY
            assert board.make_move(row, col, player) is True
            assert board.square(row, col) == player


@pytest.mark.parametrize("invalid_player", invalid_players)
@pytest.mark.parametrize("rows,cols", board_sizes)
def test_empty_board_make_move_invalid_player(
    rows: int, cols: int, invalid_player: Player
) -> None:
    for row in range(rows):
        for col in range(cols):
            board = Board(rows, cols)
            assert board.square(row, col) == Player.EMPTY
            assert board.make_move(row, col, invalid_player) is False
            assert board.square(row, col) == Player.EMPTY


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
            assert board.make_move(row, col, player1) is True
            assert board.make_move(row, col, player2) is False
