"""Challenge Question 04 - Dict Function Writing"""


def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Produces a dictionary where the keys are the items of the first list and the values are the corresponding items at the same index of the second list."""
    if len(str_list) != len(int_list) or not str_list or not int_list:
        return {}
    result = {}
    for i in range(len(str_list)):
        result[str_list[i]] = int_list[i]
    return result