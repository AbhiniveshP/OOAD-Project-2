from Canine import *

class Wolf(Canine):

    def __init__(self, name, roamer):
        super().__init__(name, roamer)

    def eat(self):
        print("{} the {} eats rabbit".format(self._name, self.__class__.__name__))
        return

    def makeNoise(self):
        print("{} the {} howls".format(self._name, self.__class__.__name__))
        return

