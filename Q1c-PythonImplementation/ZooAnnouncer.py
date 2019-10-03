from Zookeeper import Task


class ZooAnnouncer:

    announcementMap = {
        Task.WAKEUP: "\nHi, this is the Zoo Announcer. The Zookeeper is about to wake the animals!\n--",
        Task.ROLLCALL: "\nHi, this is the Zoo Announcer. The Zookeeper is about to do a roll call!\n--",
        Task.FEED: "\nHi, this is the Zoo Announcer. The Zookeeper is about to feed the animals!\n--",
        Task.LETROAM: "\nHi, this is the Zoo Announcer. The Zookeeper is about to let the animals roam about!\n--",
        Task.PUTTOBED: "\nHi, this is the Zoo Announcer. The Zookeeper is about to put the animals to bed!\n--",
    }

    zookeeper = None

    def __init__(self, zookeeper: 'Zookeeper'):
        self.zookeeper = zookeeper
        self.zookeeper.add_observer(self)

    def update(self, task: Task):
        print(self.announcementMap[task])

    def unsubscribe(self):
        self.zookeeper.remove_observer(self)
