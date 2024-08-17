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
        self.lenght = 1

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
        self.lenght +=1
        return True


myLinkedList = DoubleLinkList(7)
myLinkedList.append(2)

myLinkedList.printList()