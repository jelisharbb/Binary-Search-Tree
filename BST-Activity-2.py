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

    def preOrderTraversal(self):
    # sorts elements in this order: root node + left subtree + right subtree
    # visit root node
        elements = [self.data]

        # visit left subtree
        if self.left:
            elements += self.left.preOrderTraversal()

        # visit right subtree
        if self.right:
            elements += self.right.preOrderTraversal()

        return elements

    def postOrderTraversal(self):
        # sorts elements in this order: left subtree + right subtree + root node
        elements = []

        # visit left subtree
        if self.left:
            elements += self.left.postOrderTraversal()

        # visit right subtree
        if self.right:
            elements += self.right.postOrderTraversal()

        # visit root node
        elements.append(self.data)

        return elements

    def search(self, value):
        # returns the root node
        if value == self.data:
            return True

        # value might be on the left subtree
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        # value might be on the right subtree
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    # function that finds the leftmost (min) node in the tree
    def findMinValue(self):
        if self.left is None:
            return self.data # returns the root node if the left subtree is empty
        return self.left.findMinValue()

    # function that finds the rightmost (max) node in the tree
    def findMaxValue(self):
        if self.right is None:
            return self.data # returns the root node if the right subtree is empty
        return self.right.findMaxValue()

    # function that deletes a node
    def deleteValue(self, value):
        if value < self.data: # visits left subtree
            if self.left:
                self.left = self.left.deleteValue(value)
        elif value > self.data: # visits right subtree
            if self.right:
                self.right = self.right.deleteValue(value)
        else:
            if self.left is None and self.right is None: # checks if leaf nodes
                return None
            if self.left is None: # returns the only child node
                return self.right
            if self.right is None: # returns the right child node
                return self.left

            minValue = self.right.findMinValue() # finds the min value from the right node
            self.data = minValue # copy the min value
            self.right = self.right.deleteValue(minValue) # then remove the duplicate bode
        
        return self

# function that will create the binary tree
def buildTree(elements):
    # first element in the set will be the root node
    root = binarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.addChild(elements[i])

    return root

if __name__ == '__main__':
    fullName = ["J", "E", "L", "I", "S", "H", "A", "R", "U", "T", "H", "B", "U", "G", "N", "O", "N"]
    fullNameTree = buildTree(fullName)

    print(f"\nBuilding tree with these elements: {fullName}")

    # prints the letter in three different techniques
    print(f"\nLetters In Order Traversal: {fullNameTree.inOrderTraversal()}")
    print(f"Letters Pre Order Traversal: {fullNameTree.preOrderTraversal()}")
    print(f"Letters Post Order Traversal: {fullNameTree.postOrderTraversal()}")

    # prints the minimum and maximum value in the tree
    print(f"\nMinimum Value: {fullNameTree.findMinValue()}")
    print(f"Maximum Value: {fullNameTree.findMaxValue()}")

    # prints if the letter is on the list
    print("\nIs the letter on the list?", fullNameTree.search("C"))
    print("Is the letter on the list?", fullNameTree.search("J"))
    print("Is the letter on the list?", fullNameTree.search("B"))