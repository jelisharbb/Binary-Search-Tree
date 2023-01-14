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

    def inOrderTraversal(self):
        # sorts elements in this order: left subtree + root node + right subtree
        elements = []

        # visit left subtree
        if self.left:
            elements += self.left.inOrderTraversal()

        # visit root node
        elements.append(self.data)

        # visit right subtree
        if self.right:
            elements += self.right.inOrderTraversal()

        return elements

    def search(self, value):
        # returns the root node
        if value == self.data:
            return
            
        # value might be on the left subtree
        if value < self.data:
            if self.left:
                self.left.search(value)
            else:
                False

# function that will create the binary tree
def buildTree(elements):
    # first element in the set will be the root node
    root = binarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.addChild(elements[i])

    return root

# allows to execute code when the file runs as a script, but not when it's imported as a module
if __name__ == '__main__':
    numbers = [15, 3, 9, 20, 12, 24, 27, 1]
    numbersTree = buildTree(numbers)
    print(f"\nNumbers In Order Traversal: {numbersTree.inOrderTraversal()}\n")