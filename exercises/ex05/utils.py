"""EX05 - `list` Utility Functions."""
__author__ = 730479825


def only_evens(numbers: list[int]) -> list[int]:
    """Checks list for even numbers and returns them if they are even."""
    evens: list[int] = []
    for num in numbers:
        if num % 2 == 0:  # % 2 of even numbers == 0 but odd == 1
            evens.append(num)
    return evens


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Takes two lists of ints and concatanates them together."""
    new_list: list[int] = []
    new_list = list_1 + list_2  # simply adding the list together
    return new_list


def sub(numbers: list[int], start: int, end: int) -> list[int]:
    """Given and lsit and 2 ints, the ints are used as indexes to return a list inside the indexes."""
    if start >= len(numbers) or end <= 0 or start >= end:  # if statements act as parameters for if indexes are wrong
        return []
    if start < 0:
        start = 0
    if end > len(numbers):
        end = len(numbers)
    result = []
    i = start
    while i < end:  # used to properly move through the indexes 
        result.append(numbers[i])
        i += 1
    return result