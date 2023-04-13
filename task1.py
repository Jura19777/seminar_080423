"""
реализовать дескрипторы для любых двух классов
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    class RadiusDescriptor:
        def __get__(self, instance, owner):
            return instance._radius

        def __set__(self, instance, value):
            if value <= 0:
                raise ValueError("Радиус должен быть положительным числом")
            instance._radius = value

    radius = RadiusDescriptor()

c = Circle(5)
print(c.radius)

c.radius = 10
print(c.radius)

c.radius = -5
print(c.radius)