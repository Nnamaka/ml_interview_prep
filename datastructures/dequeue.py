class Dequeue:
    def __init__(self) -> None:
        self.deque = []

    # add emlement from the right
    def addfromright(self,dataval):
        if dataval not in self.deque:
            self.deque.append(dataval)
        else:
            print("Element already exist")

    # add element from the left
    def addfromleft(self, dataval):
        if dataval not in self.deque:
            self.deque.insert(0, dataval)
        else:
            print("Element already exist")

    # remove element from the right
    def pop(self):
        if len(self.deque) <= 0:
            return None
        
        return self.deque.pop()
    
    # remove element from the left
    def popfromleft(self):
        if len(self.deque) <= 0:
            return None
        
        return self.deque.pop(0)
    
    # show elements
    def show(self):
        print(self.deque)
    

Thedeque = Dequeue()
Thedeque.addfromright('mon')
Thedeque.addfromright('tues')

Thedeque.show()

Thedeque.addfromleft('wed')
Thedeque.addfromleft('thurs')

Thedeque.show()

Thedeque.pop()
Thedeque.popfromleft()

Thedeque.show()
