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

    # function that calculates the sum of all values in the tree
    def sumValue(self):
        leftSum = self.left.sumValue() if self.left else 0
        rightSum = self.right.sumValue() if self.right else 0
        return leftSum + self.data + rightSum

    # function that deletes a node
    def deleteValue(self, value):
        if value < self.data: # visits left subtree
            if self.left:
                self.left.deleteValue(value)
        elif value > self.data: # visits right subtree
            if self.right:
                self.right.deleteValue(value)
        else:
            if self.left is None and self.right is None: # checks if leaf nodes
                return None
            elif self.left is None: # returns the only child node
                return self.right
            elif self.right is None: # returns the right child node
                return self.right

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

# allows to execute code when the file runs as a script, but not when it's imported as a module
if __name__ == '__main__':
    numbers = [15, 3, 9, 20, 12, 24, 27, 1]
    numbersTree = buildTree(numbers)

    # # testing
    # print(f"\nNumbers In Order Traversal: {numbersTree.inOrderTraversal()}")
    # searchedValue = input("Enter the number you want to search: ")
    # print(f"Searched Value {searchedValue}: {numbersTree.search(int(searchedValue))}\n")

    # # tested strings as elements
    # fruits = ["Mango", "Papaya", "Apple", "Pears", "Melon", "Watermelon", "Avocado"]
    # fruitsTree = buildTree(fruits)

    # print("\nIs the fruit on the list?", fruitsTree.search("Melon"))
    # print("Is the fruit on the list?", fruitsTree.search("Pears"))
    # print("Is the fruit on the list?", fruitsTree.search("Banana"))

    # print(f"\nFruits In Order Traversal: {fruitsTree.inOrderTraversal()}\n")

    print(f"\nNumbers: {numbers}")
    print(f"Minimum Value: {numbersTree.findMinValue()}")
    print(f"Maximum Value: {numbersTree.findMaxValue()}")
    print(f"Summation of Values: {numbersTree.sumValue()}")
    print(f"Numbers In Order Traversal: {numbersTree.inOrderTraversal()}")
    print(f"Numbers Pre Order Traversal: {numbersTree.preOrderTraversal()}")
    print(f"Numbers Post Order Traversal: {numbersTree.postOrderTraversal()}\n")