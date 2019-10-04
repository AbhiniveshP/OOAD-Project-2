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
import os, sys

class Zookeeper:

    # list of Animals is kept as an attribute of Zookeeper class
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

        if not os._exists('out'):                   # if out folder doesn't exist, then create one
            os.mkdir('out')

        sys.stdout = open(os.path.join('out', 'dayAtTheZoo.out'), 'w')      # write all print statements to a file

        # call wakeAnimals(), rollCallAnimals(), feedAnimals(), letAnimalsRoam(), putAnimalsToBed() in the same order
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
        '''
        :return: wakeUp() list of Animals one at a time
        '''
        for animal in self.animalsList:
            animal.wakeUp()
        return

    def feedAnimals(self):
        '''
        :return: feedAnimals() list of Animals one at a time
        '''
        for animal in self.animalsList:
            animal.eat()
        return

    def letAnimalsRoam(self):
        '''
        :return: lets list of Animals roam one at a time
        '''
        for animal in self.animalsList:
            animal.roam()
        return

    def rollCallAnimals(self):
        '''
        :return: allows roll call list of Animals one at a time.
        '''
        for animal in self.animalsList:
            animal.makeNoise()
        return

    def putAnimalsToBed(self):
        '''
        :return: allows list of Animals put to bed one at a time.
        '''
        for animal in self.animalsList:
            animal.sleep()
        return

if __name__ == '__main__':
    zookeeper = Zookeeper()                     # Create Zookeeper() class and instantiate an object named zookeeper
    zookeeper.main()                            # Call main method of zookeeper object