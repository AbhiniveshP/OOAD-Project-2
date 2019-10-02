from Feline import *

class Lion(Feline):

    def __init__(self, name, roamer):
        super().__init__(name, roamer)

    def eat(self):
        print("{} the {} eats gazelle".format(self._name, self.__class__.__name__))
        return

    def makeNoise(self):
        print("{} the {} roars".format(self._name, self.__class__.__name__))
        return