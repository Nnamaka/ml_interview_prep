class Queue:
    def __init__(self) -> None:
        self.queue = []

    # insert element into queur
    def addtoq(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False
    
    # get size of queue
    def size(self):
        return len(self.queue)
    
    # show the elements in the queue
    def show(self):
        print(self.queue)

    # remove elements from the queue
    def removefromq(self):
        if len(self.queue) <= 0:
            print("No elements in the queue")
        else:
            return self.queue.pop()

    
TheQueue = Queue()
TheQueue.addtoq('mon')
TheQueue.addtoq('Tue')
TheQueue.addtoq('wed')
TheQueue.addtoq('thurs')

TheQueue.show()
print(TheQueue.size())

print(TheQueue.removefromq())

TheQueue.show()