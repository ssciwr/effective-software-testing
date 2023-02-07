from effective_software_testing.board import Board, Square


def test_empty_1x1_board() -> None:
    board = Board(1, 1)
    assert board.n_cols == 1
    assert board.n_rows == 1
    assert board.square(0, 0) == Square.EMPTY
