import math

class Point:

    def __init__(self, x=0, y=0):
        self.move(x,y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2
        )

# p1 = Point()
# p2 = Point()
# p1.x = 5
# p1.y = 7
# p2.x = 2
# p2.y = 4
# # print(p1.x, p1.y)
# # print(p2.x, p2.y)
# p = Point()
# p.reset()
# print(p.x, p.y)
#
# print(p1.calculate_distance(p2))

point1 = Point()
point2 = Point()

point1.reset()
point2.move(5,0)
print(point2.calculate_distance(point1))
assert (point2.calculate_distance(point1)) == (point2.calculate_distance(point1))
point1.move(3,4)
print((point1.calculate_distance(point2)))
print((point1.calculate_distance(point1)))

point3 = Point(5,37)
print(point3.x,point3.y)



