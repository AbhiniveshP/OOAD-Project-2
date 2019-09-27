from Pachyderm import *

class Rhino(Pachyderm):

    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print("{} the {} eats grass".format(self._name, self.__class__.__name__))
        return

    def makeNoise(self):
        print("{} the {} grunts".format(self._name, self.__class__.__name__))
        return

