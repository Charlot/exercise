import math


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, v):
        self._x = v

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, v):
        self._y = v


class Rectangle:

    def __init__(self):
        self._corner = None
        self._width = None
        self._height = None

    @property
    def corner(self):
        """
        左下顶点
        """
        return self._corner

    @corner.setter
    def corner(self, v):
        self._corner = v

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, v):
        self._width = v

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, v):
        self._height = v


class Circle:
    def __init__(self):
        self._center = None
        self._radius = None

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, v):
        self._center = v

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, v):
        self._radius = v

    @classmethod
    def point_in_circle(cls, circle, point):
        """
        点是否在圆中
        """
        distance = math.sqrt(
            math.pow(circle.center.x-point.x, 2) + math.pow(circle.center.y-point.y, 2))
        print(distance)
        return distance <= circle.radius

    @classmethod
    def rectangle_in_circle(cls, circle, rectangle):
        """
        矩形是否在圆中
        1. 判断矩形所有顶点判断是否在圆中
        2. 判断相对于圆心最远的点是否在圆中
        """
        
        pass

if __name__ == '__main__':
    circle = Circle()
    circle.center = Point(0, 0)
    circle.radius = 10

    point = Point(5, 5)

    print(Circle.point_in_circle(circle, point))
