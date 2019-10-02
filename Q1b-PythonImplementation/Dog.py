from Canine import *

class Dog(Canine):

    def __init__(self, name, roamer):
        super().__init__(name, roamer)

    def eat(self):
        print("{} the {} eats bone".format(self._name, self.__class__.__name__))
        return

    def makeNoise(self):
        print("{} the {} growls".format(self._name, self.__class__.__name__))
        return
