import os
import sys

from Cat import *
from Dog import *
from Elephant import *
from Hippo import *
from Lion import *
from Rhino import *
from Tiger import *
from Wolf import *
# from . import ZooAnnouncer
# from ZooAnnouncer import *
from enum import Enum


class Task(Enum):
    WAKEUP = 1
    ROLLCALL = 2
    FEED = 3
    LETROAM = 4
    PUTTOBED = 5

class Zookeeper:

    zoo_announcers = []

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

    def add_observer(self, zoo_announcer: 'ZooAnnouncer'):
        self.zoo_announcers.append(zoo_announcer)

    def notify_observers(self, task: Task):
        for announcer in self.zoo_announcers:
            announcer.update(task)

    def remove_observer(self, zoo_announcer: 'ZooAnnouncer'):
        self.zoo_announcers.remove(zoo_announcer)

    def wakeAnimals(self):
        self.notify_observers(Task.WAKEUP)
        for animal in self.animalsList:
            animal.wakeUp()
        return

    def feedAnimals(self):
        self.notify_observers(Task.FEED)
        for animal in self.animalsList:
            animal.eat()
        return

    def letAnimalsRoam(self):
        self.notify_observers(Task.LETROAM)
        for animal in self.animalsList:
            animal.roam()
        return

    def rollCallAnimals(self):
        self.notify_observers(Task.ROLLCALL)
        for animal in self.animalsList:
            animal.makeNoise()
        return

    def putAnimalsToBed(self):
        self.notify_observers(Task.PUTTOBED)
        for animal in self.animalsList:
            animal.sleep()
        return
