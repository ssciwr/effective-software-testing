from __future__ import annotations
from effective_software_testing.board import Board
from hypothesis import given, assume, example
import hypothesis.strategies as st


# sample n from integers in the range 0 <= n <= 99
@given(n=st.integers(min_value=0, max_value=99))
@example(n=3)  # always include n=3
def test_property_empty_board_game_not_over(n: int) -> None:
    board = Board(n)
    assert board.n == n
    assert board.game_is_over is False


@given(n=st.integers(1, 12), x=st.integers(0, 11), y=st.integers(0, 11))
def test_property_empty_board_is_empty_with_assume(n: int, x: int, y: int) -> None:
    assume(x < n)  # if x >= n we re-sample n,x,y
    assume(y < n)
    # assume works but quickly gets inefficient if many inputs do not satisfy our assumptions
    board = Board(n)
    assert board.square(x, y) is None


# using composite is a more efficient way to sample from our desired distribution of values
@st.composite
def sample_valid_n_x_y(draw: st.DrawFn) -> tuple[int, int, int]:
    max_board_n = 12
    n = draw(st.integers(1, max_board_n))
    x = draw(st.integers(0, n - 1))
    y = draw(st.integers(0, n - 1))
    return n, x, y


@given(n_x_y=sample_valid_n_x_y())
def test_property_empty_board_is_empty_with_composite(
    n_x_y: tuple[int, int, int],
) -> None:
    # no assume required here as all the x,y we generate are < n
    n, x, y = n_x_y
    board = Board(n)
    assert board.square(x, y) is None
