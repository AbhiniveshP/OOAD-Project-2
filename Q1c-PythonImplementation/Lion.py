from Feline import *

class Lion(Feline):

    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print("{} the {} eats gazelle".format(self._name, self.__class__.__name__))
        return

    def makeNoise(self):
        print("{} the {} roars".format(self._name, self.__class__.__name__))
        return