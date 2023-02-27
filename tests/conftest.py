import pytest
from effective_software_testing.board import Board
from effective_software_testing.player import Player


@pytest.fixture()
def board_2x_2o() -> Board:
    # <XX-|OO-|--->
    board = Board()
    assert board.make_move(0, 0, Player.CROSS) is True
    assert board.make_move(1, 0, Player.CIRCLE) is True
    assert board.make_move(0, 1, Player.CROSS) is True
    assert board.make_move(1, 1, Player.CIRCLE) is True
    return board
