class Animal(object):

    def __init__(self, name):
        self._name = name

    def sleep(self):
        print("{} the {} is sleeping".format(self._name, self.__class__.__name__))
        return

    def wakeUp(self):
        print("{} the {} has woken up".format(self._name, self.__class__.__name__))
        return

    def eat(self):
        pass

    def roam(self):
        pass

    def makeNoise(self):
        pass