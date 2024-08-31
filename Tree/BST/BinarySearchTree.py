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

    def breadFirstSearch(self):
        queue = []
        results = []

        temp = self.root
        queue.append(temp)

        while len(queue) > 0:
            element = queue.pop(0)
            results.append(element.value)

            if element.left is not None:
                queue.append(element.left)
            
            if element.right is not None:
                queue.append(element.right)
        return results

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return results

    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        
        traverse(self.root)
        return results


binarySearchTree = BinarySearchTree()
binarySearchTree.insert(47)
binarySearchTree.insert(21)
binarySearchTree.insert(76)
binarySearchTree.insert(18)
binarySearchTree.insert(27)
binarySearchTree.insert(52)
binarySearchTree.insert(82)

# print(binarySearchTree.root.value)
# print(binarySearchTree.root.left.value)
# print(binarySearchTree.root.right.value)

# print(binarySearchTree.contain(1))
# print(binarySearchTree.breadFirstSearch())
print(binarySearchTree.dfs_in_order())