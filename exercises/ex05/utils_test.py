"""Unit tests for only_evens, concat, and sub."""
__author__ = "730479825"

from exercises.ex05.utils import only_evens, sub, concat


# only_evens 
def test_with_only_evens() -> None:
    """Tests to see that out of a list of only evens, they are all returned."""
    test_list: list[int] = [2, 4, 6]
    assert only_evens(test_list) == [2, 4, 6]


def test_with_only_odds() -> None:
    """Tests to see that out of a list of only odds, none are returned."""
    test_list: list[int] = [1, 3, 5]
    assert only_evens(test_list) == []


def test_with_empty_list() -> None:
    """Tests to see that out of a empyt list, nothing is returned."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


# concat
def test_with_two_regular_lists() -> None:
    """Tests to check if it is correctly adding two regular lists together."""
    test_list_one: list[int] = [1, 2, 3]
    test_list_two: list[int] = [4, 5, 6]
    assert concat(test_list_one, test_list_two) == [1, 2, 3, 4, 5, 6]


def test_with_one_empty() -> None:
    """Tests to check if it is correctly adding one regular list to an empty list."""
    test_list_one: list[int] = [1, 2, 3]
    test_list_two: list[int] = []
    assert concat(test_list_one, test_list_two) == [1, 2, 3]


def test_with_two_empty() -> None:
    """Tests to check if it is correctly adding two empty lists together."""
    test_list_one: list[int] = []
    test_list_two: list[int] = []
    assert concat(test_list_one, test_list_two) == []


# sub
def test_with_valid_indexes() -> None:
    """Test to see that it correctly uses valid indexes to return values between them."""
    test_list: list[int] = [20, 30, 40, 50, 60]
    start: int = 1
    end: int = 4
    assert sub(test_list, start, end) == [30, 40, 50]


def test_with_negative_start() -> None:
    """Test to see that it correctly changes a negative start to a start of 0."""
    test_list: list[int] = [20, 30, 40, 50, 60]
    start: int = -365
    end: int = 4
    assert sub(test_list, start, end) == [20, 30, 40, 50]


def test_with_end_greater_then_length() -> None:
    """Test to see that it correctly changes a end index that is greater then the length of the list to simply the length of the list."""
    test_list: list[int] = [20, 30, 40, 50, 60]
    start: int = 1
    end: int = 365
    assert sub(test_list, start, end) == [30, 40, 50, 60]