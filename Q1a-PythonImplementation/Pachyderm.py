from Animal import *

class Pachyderm(Animal):

    def __init__(self, name):
        super().__init__(name)

    # The second level of hierarchy overrides the roam() method
    def roam(self):
        print("{} the {} stomps".format(self._name, self.__class__.__name__))
        return

    # abstract methods eat() and makeNoise() to be implemented in subclasses
    def eat(self):
        pass

    def makeNoise(self):
        pass