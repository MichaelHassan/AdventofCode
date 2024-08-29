
import pytest

from elves import calc_surface_area, get_smallest_side


def test_calc_surface_area():
    result = calc_surface_area(2, 3, 4)
    assert result == 52


def test_get_smallest_side():

    result = get_smallest_side([2, 3, 4])
    assert result == 6
