# a bst is a binary tree where the left-tree node elements are less than or
# equal to the parent node and the right-tree node elements are greater than 
# the parent node

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
        
    # pre-order trasversal root -> left -> right
    def preorderTrasversal(self, root):
        res = []

        if root:
            res.append(root.data)
            res = res + self.preorderTrasversal(root.left)
            res = res + self.preorderTrasversal(root.right)
        return res
    
    # post-order trasversal left -> right -> root
    def postorderTrasversal(self, root):
        res = []

        if root:
            # left, right, root
            res = res + self.postorderTrasversal(root.left)
            res = res + self.postorderTrasversal(root.right)
            res.append(root.data)
        return res
    
    # searching a BST
    def findval(self, val):
        if self.data > val:
            if self.left is None:
                return str(val) + " not found⚠"
            return self.left.findval(val)
        elif self.data < val:
            if self.right is None:
                return str(val) + " not found⚠"
            return self.right.findval(val)
        else:
            return str(val) + " found✅"
        
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.findval(7))
print(root.findval(14))