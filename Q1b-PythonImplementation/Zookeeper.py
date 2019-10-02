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
import Roamer
import os, sys

class Zookeeper:

    # The strategy pattern is applied here.  Defined in the animal class (in Animal.py),
    # each animal contains a Roamer object (defined in Roamer.py).  The Roamer is an abstract class which is implemented
    # by three concrete classes: Runner, Stalker, Stomper.  Each animal contains a Roamer which is instantiated
    # with a concrete class on instantiation of the Animal.  When Animal.roam() is called, it delegates the responsibility
    # to the Roamer it was instantiated with.
    animalsList = [
        Cat('Carl', Roamer.Stalker()), Cat('Candy', Roamer.Stalker()),
        Dog('Doris', Roamer.Runner()), Dog('Dan', Roamer.Runner()),
        Elephant('Eric', Roamer.Stomper()), Elephant('Earl', Roamer.Stomper()),
        Hippo('Harry', Roamer.Stomper()), Hippo('Humphrey', Roamer.Stomper()),
        Lion('Leopold', Roamer.Stalker()), Lion('Larry', Roamer.Stalker()),
        Rhino('Rory', Roamer.Stomper()), Rhino('Rodger', Roamer.Stomper()),
        Tiger('Terrance', Roamer.Stalker()), Tiger('Time', Roamer.Stalker()),
        Wolf('Wallace', Roamer.Runner()), Wolf('Wendy', Roamer.Runner())
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