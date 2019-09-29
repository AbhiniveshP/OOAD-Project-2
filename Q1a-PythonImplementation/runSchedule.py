import os
import sys

from ZooAnnouncer import ZooAnnouncer
from Zookeeper import Zookeeper

if not os.path.exists('out'):
    os.mkdir('out')

sys.stdout = open(os.path.join('out', 'dayAtTheZoo.out'), 'w')

zookeeper = Zookeeper()

zoo_announcer = ZooAnnouncer(zookeeper)

zookeeper.wakeAnimals()
zookeeper.rollCallAnimals()
zookeeper.feedAnimals()
zookeeper.letAnimalsRoam()
zookeeper.putAnimalsToBed()

zoo_announcer.unsubscribe()
