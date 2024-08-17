class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



# insert new node 1st postion
def insert1stPosition(value):
    # create new node 
    newNode = Node(value)
    # get current headNode 
    headNode = node1
    # insert new Node as head Node 
    node1 = newNode
    # link previous headNode as current headNode next element
    node1.next = headNode


#printing the linked list
def traversingTheLinkList(head):
    current = head
    while current is not None:
        print(current.data, end="->")
        current = current.next
    print("None")


# find the lowest value
def findTheLowestValue(head):
    lowestValue=head.data
    curentNode=head.next

    while curentNode:
        if curentNode.data < lowestValue:
            lowestValue = curentNode.data
        curentNode=curentNode.next
    return lowestValue



# creating node
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)


# connecting node each other
node1.next = node2
node2.next = node3
node3.next = node4

# traversing the value
traversingTheLinkList(node1)

#minimum value
# minValue = findTheLowestValue(node1)
# print('Lowest value is: ', minValue)
    


