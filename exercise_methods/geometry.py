

from cmath import pi


def area(radius):
    area_ans = radius*radius*3.1459
    return round(area_ans, 2)

def hype(side1, side2):
    hype_ans = (side1**2 + side2**2)**(1/2)
    return round(hype_ans, 2)