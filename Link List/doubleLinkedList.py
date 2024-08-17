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
    
    def pop_first(self):
        if self.length == 0:
            return False
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head

            new_head_value = temp.next
            new_head_value.prev = None
            self.head = new_head_value
        
        self.length -= 1
        return True

    #get value of specific index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp
    
    # change value of specific index node
    def set_value(self, index, value):
        temp = self.get(2)

        if temp:
            temp.value = value
            return True
        return False





myLinkedList = DoubleLinkList(7)
myLinkedList.append(5)
myLinkedList.append(3)
# myLinkedList.prepend(4)
# myLinkedList.pop_first()
# print("Print Index 2 Value: ",myLinkedList.get(2).value)

myLinkedList.printList()


print("Print After Set Value Of Index 1: ")
myLinkedList.set_value(1, 10)
myLinkedList.printList()