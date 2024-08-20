# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None



# # insert new node 1st postion
# def insert1stPosition(value):
#     # create new node 
#     newNode = Node(value)
#     # get current headNode 
#     headNode = node1
#     # insert new Node as head Node 
#     node1 = newNode
#     # link previous headNode as current headNode next element
#     node1.next = headNode


# #printing the linked list
# def traversingTheLinkList(head):
#     current = head
#     while current is not None:
#         print(current.data, end="->")
#         current = current.next
#     print("None")


# # find the lowest value
# def findTheLowestValue(head):
#     lowestValue=head.data
#     curentNode=head.next

#     while curentNode:
#         if curentNode.data < lowestValue:
#             lowestValue = curentNode.data
#         curentNode=curentNode.next
#     return lowestValue



# # creating node
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)


# # connecting node each other
# node1.next = node2
# node2.next = node3
# node3.next = node4

# # traversing the value
# traversingTheLinkList(node1)

# #minimum value
# # minValue = findTheLowestValue(node1)
# # print('Lowest value is: ', minValue)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    # print list 
    def printList(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def append(self, value):

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        

    def pop(self):
        temp = self.head
        prev = temp
        while (temp.next):
            prev = temp
            temp = temp.next
        
        self.tail = prev
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head == new_node
            self.tail == new_node
        else:
            head_node = self.head
            self.head = new_node
            self.head.next = head_node

        self.length +1

    def pop_first(self):
        if self.length == 0:
            return False

        head_node = self.head
        self.head = head_node.next
        head_node.next = None
        self.length -=1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp


    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return temp

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            head_val = self.head
            self.head = new_node
            self.head.next = head_val
        else:
            index_value = self.get(index)
            prev_value = self.get(index - 1)

            new_node.next = index_value
            prev_value.next = new_node
        return new_node

    def remove(self):
        return True

my_link_list = LinkedList(10)
my_link_list.append(20)
my_link_list.append(30)
my_link_list.prepend(5)
# my_link_list.pop_first()
# my_link_list.set_value(0, 5)
# my_link_list.insert(2, 15)
my_link_list.printList()
    


