from Animal import *

class Canine(Animal):

    def __init__(self, name):
        super().__init__(name)

    def roam(self):
        print("{} the {} runs".format(self._name, self.__class__.__name__))
        return

    def eat(self):
        pass

    def makeNoise(self):
        pass

