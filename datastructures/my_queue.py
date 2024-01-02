# implementation of queue from scratch
# a queue is a first in first out kind of datastructure

class Node:
    def __init__(self, customer: str) -> None:
        self.next = None
        self.data = customer

class Quueue:

    def __init__(self) -> None:
        self.head = None

    def push(self,value: str):
        """
            This function takes in a string and adds it to 
            the queue
            Args:
                value (str): the customer in the queue
            Returns:
                None
        """
        newNode = Node(customer=value)

        nextNode = self.head

        if nextNode is not None :
            while(nextNode.next):
                nextNode = nextNode.next
            nextNode.next = newNode
        else:
            self.head = newNode

    def printQueue(self):
        """
            This function prints the elements of the queue
            Args:
                no argument
            Returns:
                no return value
        """
        firstNode = self.head
        while(firstNode.next):
            print(firstNode.data)
            firstNode = firstNode.next
    def pop(self):
        """
            This function removes an element from the queue
            takes out argument from the list
            Args:
                no argument
        """
        showHead = self.head
        self.head = self.head.next
        print(showHead.data)
        return showHead.data


customerQueue = Quueue()
customerQueue.push(value="John")
customerQueue.push("mary")
customerQueue.push("Junior")
customerQueue.push("Junior2")
customerQueue.push("Junior3")

customerQueue.printQueue()

print(f'\nfirst customer {customerQueue.pop()} has finished buying ice cream\n')
print(f'the remaining customers are')

customerQueue.printQueue()

