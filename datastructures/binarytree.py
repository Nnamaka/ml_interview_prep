# implementation of binary tree datastructure with python
# youtube video coming soon

class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    # in-order trasversal
    def inorderTrasversal(self, root):
        res = []

        if root:
            res = self.inorderTrasversal(root.left)
            res.append(root.data)
            res = res + self.inorderTrasversal(root.right)
        return res
        
    # pre-order trasversal
    def preorderTrasversal(self, root):
        res = []

        if root:
            res.append(root.data)
            res = res + self.preorderTrasversal(root.left)
            res = res + self.preorderTrasversal(root.right)
        return res
    
    # post-order trasversal
    def postorderTrasversal(self, root):
        res = []

        if root:
            # left, right, root
            res = res + self.postorderTrasversal(root.left)
            res = res + self.postorderTrasversal(root.right)
            res.append(root.data)
        return res
    
# create root node
root = Node(12)

# insert data to nodes
root.insert(6)
root.insert(14)
root.insert(3)

# print elements of a binary list
root.printTree()

root.insert(19)
root.insert(31)
root.insert(42)

# trasversing a list
print(root.inorderTrasversal(root))
print(root.preorderTrasversal(root))
print(root.postorderTrasversal(root))
