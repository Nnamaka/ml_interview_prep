class Stack:
    def __init__(self) -> None:
        self.stack = []

    # add element to the stack
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
        
    # look at or peek at the top of the stack
    def peek(self):
        return self.stack[-1]
    
    # pop element from stack
    def remove(self):
        if len(self.stack) <= 0:
            return 'No element in Stack'
        else:
            return self.stack.pop()
        
    # show values in stack
    def show(self):
        if len(self.stack) <= 0:
            print(None)
        else:
            print(self.stack)

    
AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")


AStack.show()
print(AStack.peek())

AStack.add("wed")
AStack.add("Thu")

AStack.show()
print(AStack.peek())

print(AStack.remove())
print(AStack.remove())

AStack.show()
