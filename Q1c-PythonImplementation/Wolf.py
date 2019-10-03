from Canine import *

class Wolf(Canine):

    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print("{} the {} eats rabbit".format(self._name, self.__class__.__name__))
        return

    def makeNoise(self):
        print("{} the {} howls".format(self._name, self.__class__.__name__))
        return

