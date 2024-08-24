class Node:
    def __init__(self, value):
        try:
            self.value = value
            self.next = None
        except Exception as e:
            print('Exception got init: ', e)


class LinkedList:
    def __init__(self, value):
        try:
            newNode = Node(value)

            self.head = newNode
            self.tail = newNode
        except Exception as e:
            print('Exception got on: ', e)

    def inQueue(self, value):
        try:
            newNode = Node(value)
            tailValue = self.tail

            tailValue.next = newNode
            self.tail = newNode

        except Exception as e:
            print('Exception on inqueue: ', e)

    def deQueue(self):
        try:
            deQueueValue = self.head
            self.head = deQueueValue.next

            return deQueueValue
        except Exception as e:
            print('Exception on dequeue: ', e)

    def printValue(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp=temp.next


queue = LinkedList(10)
queue.inQueue(20)
queue.inQueue(30)
print('deQueue value: ',queue.deQueue().value)
queue.printValue()