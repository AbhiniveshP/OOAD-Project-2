class Animal(object):

    def __init__(self, name):
        self._name = name

    # sleep() and wakeUp() methods are common to all Animal subclasses
    def sleep(self):
        print("{} the {} is sleeping".format(self._name, self.__class__.__name__))
        return

    def wakeUp(self):
        print("{} the {} has woken up".format(self._name, self.__class__.__name__))
        return

    # abstract methods of eat(), roam() and makeNoise() to be implemented in subclasses
    def eat(self):
        pass

    def roam(self):
        pass

    def makeNoise(self):
        pass