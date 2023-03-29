"""Test functions for Dictionary Functions."""
__author__ = '730479825'

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


# invert
def test_invert_edge_case() -> None:
    """Test with an empty dictionary."""
    d = {}
    assert invert(d) == {}


def test_invert_use_case_1() -> None:
    """Test with a dictionary that has different vlaues."""
    d = {"apple": "1", "banana": "2", "orange": "3"}
    assert invert(d) == {"1": "apple", "2": "banana", "3": "orange"}


def test_invert_use_case_2() -> None:
    """Test with a dictionary that has multiple same values."""
    with pytest.raises(KeyError):
        d = {"apple": "1", "banana": "2", "orange": "1"}
        invert(d)


# favorite_colors
def test_favorite_color_edge_case() -> None:
    """Test with a dict in which one entry is flipped."""
    d = {"yellow": "Mark", "Ezri": "yellow", "Kris": "blue"}
    assert favorite_color(d) != "yellow"
    

def test_favorite_color_use_case_1() -> None:
    """Test with a dictionary containing multiple people with the same favorite color."""
    d = {"Alice": "red", "Bob": "green", "Charlie": "red", "Dave": "yellow"}
    assert favorite_color(d) == "red"


def test_favorite_color_use_case_2() -> None:
    """Test with a dictionary that has a tie of favorites."""
    d = {"Alice": "red", "Bob": "green", "Charlie": "red", "Dave": "green"}
    assert favorite_color(d) == "red"


# count
def test_count_edge_case() -> None:
    """Test with an empty list."""
    input_list = []
    assert count(input_list) == {}


def test_count_use_case_1() -> None:
    """Test with a regular list of single indexes."""
    input_list = ['apple', 'banana', 'orange']
    assert count(input_list) == {'apple': 1, 'banana': 1, 'orange': 1}


def test_count_use_case_2() -> None:
    """Test with a list that has multiple of the same indexes."""
    input_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    assert count(input_list) == {'apple': 2, 'banana': 3, 'orange': 1}