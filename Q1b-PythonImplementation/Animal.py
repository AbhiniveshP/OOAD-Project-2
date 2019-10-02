class Animal(object):

    def __init__(self, name, roamer):
        self._name = name
        self._roamer = roamer

    def sleep(self):
        print("{} the {} is sleeping".format(self._name, self.__class__.__name__))
        return

    def wakeUp(self):
        print("{} the {} has woken up".format(self._name, self.__class__.__name__))
        return

    def eat(self):
        pass
    
    # As part of the strategy pattern, the Animal delegates roaming responsibility to the Roamer.  It passes
    # its name and species to Roamer.roam() when Animal.roam() is called.
    def roam(self):
        self._roamer.roam(self._name, self.__class__.__name__)

    def makeNoise(self):
        pass