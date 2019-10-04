from Pachyderm import *

class Hippo(Pachyderm):

    def __init__(self, name):
        super().__init__(name)

    # eat() method implemented at the lowest hierarchy
    def eat(self):
        print("{} the {} eats reeds".format(self._name, self.__class__.__name__))
        return

    # makeNoise() method implemented at the lowest hierarchy
    def makeNoise(self):
        print("{} the {} grunts".format(self._name, self.__class__.__name__))
        return