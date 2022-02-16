import random


def random_color():
    """
    Returns random color from the list.
    Used for drawing bypass connections to mixers.
    """
    colors = ["#299617", "#FFAA1D", "#2243B6", "#FF7A00", "#0048BA", "#E936A7"]
    return colors[random.randint(0, len(colors)-1)]