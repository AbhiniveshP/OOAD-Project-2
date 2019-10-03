from Feline import *
import random

class Cat(Feline):

    def __init__(self, name):
        super().__init__(name)

    def randomBehaviour(self):

        randomNumber = random.randint(0, 4)
        if randomNumber == 0:
            self.wakeUp()
        elif randomNumber == 1:
            self.roam()
        elif randomNumber == 2:
            self.eat()
        elif randomNumber == 3:
            self.makeNoiseCat()
        elif randomNumber == 4:
            self.sleep()
        else:
            self.sleep()
        return

    def eat(self):
        print("{} the {} eats mice".format(self._name, self.__class__.__name__))
        return

    def makeNoiseCat(self):
        print("{} the {} purrs".format(self._name, self.__class__.__name__))
        return

    def makeNoise(self):
        self.randomBehaviour()
        return
