"""
question：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法
author：吕梦龙
date：2023-09-08
"""
from math import sqrt


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        return sqrt(dx ** 2 + dy ** 2)

    def address(self):
        return f"({self.x}, {self.y})"

if __name__ == '__main__':
    p1 = Point()
    p2 = Point(1, 2)
    print(p1.address())
    print(p2.address())
    p2.move(3, 4)
    print(p2.address())
    print(p1.distance(p2))
