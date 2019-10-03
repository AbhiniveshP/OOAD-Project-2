from Animal import *
from Canine import *
from Feline import *
from Pachyderm import *
from Dog import *
from Wolf import *
from Cat import *
from Lion import *
from Tiger import *
from Elephant import *
from Rhino import *
from Hippo import *
from . import Dog, Wolf, Cat, Lion, Tiger, Elephant, Rhino, Hippo
import os, sys

class Zookeeper:

    animalsList = [
        Cat('Carl'), Cat('Candy'),
        Dog('Doris'), Dog('Dan'),
        Elephant('Eric'), Elephant('Earl'),
        Hippo('Harry'), Hippo('Humphrey'),
        Lion('Leopold'), Lion('Larry'),
        Rhino('Rory'), Rhino('Rodger'),
        Tiger('Terrance'), Tiger('Time'),
        Wolf('Wallace'), Wolf('Wendy')
    ]

    def main(self):

        if not os._exists('out'):
            os.mkdir('out')

        sys.stdout = open(os.path.join('out', 'dayAtTheZoo.out'), 'w')

        print("The Zookeeper is waking up the animals:\n---")
        self.wakeAnimals()
        print("\nThe Zookeeper is doing roll call:\n---")
        self.rollCallAnimals()
        print("\nThe Zookeeper is feeding the animals:\n---")
        self.feedAnimals()
        print("\nThe Zookeeper is letting the animals roam about:\n---")
        self.letAnimalsRoam()
        print("\nThe Zookeeper is putting the animals to bed:\n---")
        self.putAnimalsToBed()

        return

    def wakeAnimals(self):
        for animal in self.animalsList:
            animal.wakeUp()
        return

    def feedAnimals(self):
        for animal in self.animalsList:
            animal.eat()
        return

    def letAnimalsRoam(self):
        for animal in self.animalsList:
            animal.roam()
        return

    def rollCallAnimals(self):
        for animal in self.animalsList:
            animal.makeNoise()
        return

    def putAnimalsToBed(self):
        for animal in self.animalsList:
            animal.sleep()
        return

if __name__ == '__main__':
    zookeeper = Zookeeper()
    zookeeper.main()