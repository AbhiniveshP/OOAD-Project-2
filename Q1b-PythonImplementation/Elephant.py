from Pachyderm import *

class Elephant(Pachyderm):

    def __init__(self, name, roamer):
        super().__init__(name, roamer)

    def eat(self):
        print("{} the {} eats tree bark".format(self._name, self.__class__.__name__))
        return

    def makeNoise(self):
        print("{} the {} trumpets".format(self._name, self.__class__.__name__))
        return

