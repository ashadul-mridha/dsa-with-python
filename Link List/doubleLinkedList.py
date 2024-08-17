class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkList:
    def __init__(self, value):
        new_node = Node(7)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        return True

    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.prev = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -=1
        return temp

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head

            new_node.prev = None
            new_node.next = temp
            self.head = new_node
        
        self.length +=1
        return True




myLinkedList = DoubleLinkList(7)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.prepend(4)
myLinkedList.pop()

myLinkedList.printList()