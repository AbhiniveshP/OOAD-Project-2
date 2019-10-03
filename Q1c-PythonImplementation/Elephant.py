from Pachyderm import *

class Elephant(Pachyderm):

    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print("{} the {} eats tree bark".format(self._name, self.__class__.__name__))
        return

    def makeNoise(self):
        print("{} the {} trumpets".format(self._name, self.__class__.__name__))
        return

