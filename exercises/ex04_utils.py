"""EX04 - `list` Utility Functions."""
__author__ = "730479825"


def all(numbers: list[int], single: int) -> bool:
    """Checks to see if the list is only comprised of the single int."""
    idx: int = 0
    count: int = 0
    running: bool = True 
    while running:
        if numbers == []:  # if blank, its false
            return False
        if numbers[idx] == single:  # if same moves to next one
            idx += 1 
            count += 1
        if count == len(numbers):  # stops once you get to the end
            running = False
            return True 
        if numbers[idx] != single:  # if different its false
            return False
    return False 
        

def max(numbers: list[int]) -> int:
    """Determines highest value int in list and returns it."""
    idx: int = 1
    max_value = numbers[0]
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")
    while idx < len(numbers):
        if numbers[idx] > max_value:  # if next number is larger then previous it becomes the new max
            max_value = numbers[idx]
        idx += 1  # repeat untill length is exausted
    return max_value


def is_equal(first: list[int], second: list[int]) -> bool:
    """Determines if the ints in the lists are equal to one another."""
    running: bool = True 
    idx_first: int = 0
    idx_second: int = 0
    count: int = 0
    while running:
        if len(first) != len(second):  # if lengths are different, its false 
            return False
        if len(first) == 0 and len(second) == 0:  # if empty you get true 
            return True
        if count == len(first):  # stop once done and return true 
            running = False
            return True 
        if first[idx_first] != second[idx_second]:  # if not equal, flase 
            return False
        if first[idx_first] == second[idx_second]:  # if equal, move to next 
            idx_first += 1
            idx_second += 1 
            count += 1
    return False