# import numpy as np
# """Representing a point. As 2D tuples"""

# def move(p, d):
#     x, y = p
#     dx, dy = d
#     return (x+dx, y+dy)

# if __name__ == "__main__":

#     p = np.array((3, 4))
#     v = np.array((1, 2))

#     # res = move(p, v)
#     # print(f"{p} + {v} = {res}")

#     print(p + v)

class Point:
    
    def __init__(self, x, y) -> None: # ran when object is created
        self.x = x # declaring an instance variable
        self.y = y

    def move(self, d): # assumes a point object (d) as input
        x = self.x + d.x
        y = self.y + d.y
        return Point(x, y)
    
    def __str__(self) -> str:
        return f"{(self.x, self.y)}"
    

if __name__ == "__main__":
    point1 = Point(2, 4) # runs the __init__ function on creation and records the instance variables
    vector = Point(1, 5)

    moved_p1 = point1.move(vector)

    assert moved_p1.x == 3 and moved_p1.y == 9

    print(moved_p1.__str__())
    print(type(moved_p1) == Point)
