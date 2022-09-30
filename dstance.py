import math
def distance(a1, a2, b1, b2):
    x = a2 - a1
    y = b2 - b1
    return math.sqrt((x ** 2) + (y ** 2))
