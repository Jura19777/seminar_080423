"""
реализовать метакласс. позволяющий создавать всегда один и тот же объект класса
"""
class Singleton(type):
    __instance__ = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = super().__call__(*args, **kwargs)
        return cls.__instance__

class MyClass(metaclass=Singleton):
    pass

a = MyClass()
b = MyClass()

print(a is b)
print(id(a))
print(id(b))