# single linked list
# we use the concept of nodes to create a singly list in python
class Node:
    def __init__(self, dataval=None) -> None:
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self) -> None:
        self.headval = None

    # traversing a singly linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    # inserting elements at the begining of linked list
    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    # inserting elements at the end of linked list
    def AtEnd(self, newdata):
        Newnode = Node(newdata)

        if self.headval is None:
            self.headval = Newnode
            return
        
        last = self.headval

        while(last.nextval):
            last = last.nextval
        
        last.nextval = Newnode


    # inserting elements between data nodes
    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        
        Newnode = Node(newdata)
        
        Newnode.nextval = middle_node.nextval
        middle_node.nextval = Newnode

    # removing an item
    def RemoveNode(self, removekey):
        Headval = self.headval

        # check if value is at the head node
        if (Headval is not None):
            if (Headval.dataval == removekey):
                self.head = Headval.nextval
                Headval = None
                return
            
        while(Headval is not None):
            if Headval.dataval == removekey:
                break
            prev = Headval
            Headval = Headval.nextval

        if Headval == None :
            return
        
        prev.next = Headval.nextval
        Headval = None


list1 = SLinkedList()
list1.headval = Node('Monday')
e2 = Node('Tuesday')
e3 = Node('Wednesday')

# connect head of singly linked list to next element
list1.headval.nextval = e2

# connect element 2 to element
e2.nextval = e3


