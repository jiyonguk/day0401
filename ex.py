import math

def getcircleArea(radius):
    return math.pow(radius,2) * math.pi


def getDountArea(r1, r2):

    area1 = getcircleArea(r1)
    area2 = getcircleArea(r2)

    return abs(area1 - area2)


if __name__ == "__main__":

    result = getDountArea(5,10)
    print(result)
    print("-------------------")
    print("-------------------")
    print("-------------------")
    print("-------------------")
    print("-------------------")