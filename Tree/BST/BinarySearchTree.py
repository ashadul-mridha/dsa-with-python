class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)

        if self.root == None:
            self.root = newNode
            return True
        
        temp = self.root
        while(True):
            if newNode.value == temp.value:
                return False
            
            if newNode.value < temp.value:
                if temp.left is None:
                    temp.left = newNode
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = newNode
                    return True
                temp = temp.right

    def contain(self, value):
        if self.root is None:
            return False
        
        temp =self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left
            if value > temp.value:
                temp = temp.right
            else:
                return True
        return False



binarySearchTree = BinarySearchTree()
binarySearchTree.insert(2)
binarySearchTree.insert(3)
binarySearchTree.insert(1)

# print(binarySearchTree.root.value)
# print(binarySearchTree.root.left.value)
# print(binarySearchTree.root.right.value)

print(binarySearchTree.contain(1))