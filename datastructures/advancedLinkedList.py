class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None

    # pushing new elements
    def push(self, Newval):
        Newnode = Node(Newval)
        Newnode.next = self.head

        if self.head is not None:
            self.head.prev = Newnode

        self.head = New