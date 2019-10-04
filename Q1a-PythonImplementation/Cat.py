from Feline import *
import random

class Cat(Feline):

    def __init__(self, name):
        super().__init__(name)

    # function to implement random behaviour which generates a random integer in the range [0, 4] and performs
    # one of the behaviours according to the integer obtained.
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

    # eat() method implemented at the lowest hierarchy
    def eat(self):
        print("{} the {} eats mice".format(self._name, self.__class__.__name__))
        return

    # makeNoiseCat() method implemented at the lowest hierarchy
    def makeNoiseCat(self):
        print("{} the {} purrs".format(self._name, self.__class__.__name__))
        return

    # makeNoise() performs random behaviour and so a separate functionality of makeNoiseCat() has been implemented above
    def makeNoise(self):
        self.randomBehaviour()
        return
