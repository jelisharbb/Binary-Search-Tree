# # Create a binary tree using my full name as the elements

class binarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            # returns the data if it already exists
            return

        if data < self.data:
            # adds data in the left subtree
            if self.left:
                self.left.addChild(data)
            else:
                self.left = binarySearchTreeNode(data)

        else:
            # adds data in the right subtree
            if self.right:
                self.right.addChild(data)
            else:
                self.right = binarySearchTreeNode(data)