import pytest

from day1 import find_pair, find_answer, find_triplets


def test_find_pair_valid():

    assert find_pair(['1721', '979', '366', '299',
                     '675', '1456'], 2020) == [1721, 299]


def test_find_answer__valid():

    assert find_answer([1721, 299]) == 514579


def test_find_answer__invalid():

    with pytest.raises(ValueError):
        find_answer([1721, 299, 333])


def test_find_triplets():

    assert find_triplets(['1721', '979', '366', '299',
                          '675', '1456'], 2020) == [979, 366, 675]
