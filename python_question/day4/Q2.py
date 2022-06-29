import math

def square(x):
    return x * x

class Coordinate:
    x=0
    y=0
    # def __init__(self,x,y):
    #     self.x=x
    #     self.y=y
    def distance(point_a, point_b):
        return math.sqrt(square(point_a.x - point_b.x) +square(point_a.y - point_b.y))


point_1 = Coordinate()
point_1.x = -1
point_1.y = 2

point_2 =Coordinate()
point_2.x = 2
point_2.y = 3
print(point_1.distance(point_2))

