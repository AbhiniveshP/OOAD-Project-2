from Canine import *

class Dog(Canine):

    def __init__(self, name):
        super().__init__(name)

    # eat() method implemented at the lowest hierarchy
    def eat(self):
        print("{} the {} eats bone".format(self._name, self.__class__.__name__))
        return

    # makeNoise() method implemented at the lowest hierarchy
    def makeNoise(self):
        print("{} the {} growls".format(self._name, self.__class__.__name__))
        return
