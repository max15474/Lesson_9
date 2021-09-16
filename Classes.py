class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Точка: ({self.x}, {self.y})'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def point_dis(self, a, b):
        return ((self.x - a) ** 2 + (self.y - b) ** 2) ** 0.5


p = Point(4, 1)
q = Point(8, -2)

print(p + q)
print(p.x, p.y)
print(p)
print(p.distance())
print(p.point_dis(3, 4))
