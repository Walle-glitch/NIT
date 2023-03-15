
########################## Övning 7 #######################################

import copy

class Punkt:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f'Punkt({self._x}, {self._y})'
    
    def flytta(self, delta_x, delta_y):
        self._x += delta_x
        self._y += delta_y

    def get_koordinater(self):
        koordinater = (self._x, self._y)
        #return print(f'nuvarande position {koordinater}')
        return koordinater


class Karaktär:
    def __init__(self, namn):
        self._namn = namn
        self._position = Punkt(0, 0)

    def byt_namn(self, nytt_namn):
        self._namn = nytt_namn

    def gå_framåt(self, steg):
        self._position.flytta(steg, 0)

    def __str__(self):
        return f'Karaktär: {self._namn} på position {self._position.get_koordinater()}'

class Spelare(Karaktär):
    def __init__(self, namn, stridsrop):
        super().__init__(namn)
        self._stridsrop = stridsrop

    def skrik(self):
        return print(self._stridsrop)

    def __str__(self):
        return f'Spelare: {self._namn} på position {self._position.get_koordinater()}'

hjälte = Karaktär('Pythonmannen')

elak_tvilling = copy.deepcopy(hjälte)

elak_tvilling.byt_namn('Pythonkopian')

Leroy = Spelare('Leroy Jenkins', 'LEEEEEEEEEROOY JENKINS!!!!')
präst = Spelare('Priest', 'Wololo!')
print(Leroy)
print(hjälte)
print(elak_tvilling)
Leroy.skrik()
präst.skrik()
Leroy.gå_framåt(4)
print(Leroy)
