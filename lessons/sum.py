"""Example function for unit tests"""

def sum(xs: list[float]) -> float: 
    """return the sum of all elements in xs"""
    total: float = 0.0
    for num in xs:
        total += num
    return total