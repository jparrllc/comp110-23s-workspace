"""EX07 - Dictionary Functions."""
__author__ = '730479825'


# invert
def invert(d: dict[str, str]) -> dict[str, str]:
    """Function that flips the keys and the values of the dictionary that is input."""
    inverted_dict: dict[str, str] = {}
    for key in d:
        value: str = d[key]  # way to get values
        if value in inverted_dict:  # raises keyerror if the vlaue is repeated or already in empty dictionary
            raise KeyError(f"KeyError: {value} already exists as a key in the inverted dictionary.")
        inverted_dict[value] = key
    return inverted_dict


# favorite_colors
def favorite_color(d: dict[str, str]) -> str:
    """Function that looks at a dictonary of names and colors and reurns which color is most prevalent."""
    colors_empty: dict[str, str] = {}
    for name in d:
        color: str = d[name]  # way to get values
        if color not in colors_empty:  # if its not found its added
            colors_empty[color] = 0
        colors_empty[color] += 1

    common: str = None
    most: int = -1
    for color in colors_empty:
        count: int = colors_empty[color]
        if count > most:
            common = color
            most = count
    return common


# count
def count(input_list: list[str]) -> dict[str, int]:
    """Function that creates a dict out of a list. Checks list for repeating indexes and makes them the keys, the number of times they are repeated becomes the vlaues."""
    empty_dict: dict[str, str] = {}
    for item in input_list:
        if item in empty_dict:
            empty_dict[item] += 1
        else:
            empty_dict[item] = 1
    return empty_dict