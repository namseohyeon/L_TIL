import math

class Coordinate:
    x=0
    y=0
    # def __init__(self,x,y):
    #     self.x=x
    #     self.y=y

def square(x):
    return x * x
def distance(point_a, point_b):
        return math.sqrt(square(point_a.x - point_b.x) +square(point_a.y - point_b.y))

point_1 = Coordinate()
point_1.x = -1
point_1.y = 2

point_2 =Coordinate()
point_2.x = 2
point_2.y = 3
print(distance(point_1, point_2))

