class Punkt:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        ny_x = self._delta_x + self._x
        ny_y = self._delta_y + self._y
        return f'({ny_x}, {ny_y})'

    def flytta(self, delta_x, delta_y):
        self._delta_x = delta_x
        self._delta_y = delta_y
        
p = Punkt(3, 4)
p.flytta(1, 1)

print(p)



