

"""
NOTE: This is a double linked list and the first and the last element should point
to each other.
also if you're having issues understanding the kind of stack operation of how elements are
added and removed from the list, you can ask gpt/berd to implement an equivalent of a "push"
function in python's "list" class to see if items are added at the front or the back
"""

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # pushing new elements
    def push(self, Newval):
        Newnode = Node(Newval)
        Newnode.next = self.head

        if self.head is not None:
            self.head.prev = Newnode

        self.head = Newnode