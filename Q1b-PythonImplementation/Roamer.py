import abc

# Roamer is an abstract class which is implemented by multiple concrete classes.
# The responsibility for roam() is delegated to a Roamer embedded in each Animal.
class Roamer(abc.ABC):
    @abc.abstractmethod
    def roam(self, name, species):
        pass

class Runner(Roamer):
    def roam(self, name, species):
        print("{} the {} runs".format(name, species))
        return

class Stalker(Roamer):
    def roam(self, name, species):
        print("{} the {} stalks".format(name, species))
        return

class Stomper(Roamer):
    def roam(self, name, species):
        print("{} the {} stomps".format(name, species))
        return