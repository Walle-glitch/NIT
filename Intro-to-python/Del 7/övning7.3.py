class Punkt:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f'punkt({self._x}, {self._y})'

p = Punkt(3, 4)
print(p)
