from Pachyderm import *

class Hippo(Pachyderm):

    def __init__(self, name, roamer):
        super().__init__(name, roamer)

    def eat(self):
        print("{} the {} eats reeds".format(self._name, self.__class__.__name__))
        return

    def makeNoise(self):
        print("{} the {} grunts".format(self._name, self.__class__.__name__))
        return