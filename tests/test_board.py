from effective_software_testing.board import Board


def test_empty_board() -> None:
    board = Board()
    assert board.get_square(0, 0) is None
