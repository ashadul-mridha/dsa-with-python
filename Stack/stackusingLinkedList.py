class Node:
    def __init__(self, value):
        try:
            self.prev = None
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

    def push(self, value):
        try:
            newNode = Node(value)
            tailValue = self.tail

            tailValue.next = newNode
            newNode.prev = tailValue
            self.tail = newNode

        except Exception as e:
            print('Exception on inqueue: ', e)

    def pop(self):
        try:
            popValue = self.tail
            self.tail = popValue.prev
            self.tail.next = None

            return popValue
        except Exception as e:
            print('Exception on dequeue: ', e)

    def printValue(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp=temp.next


queue = LinkedList(10)
queue.push(20)
queue.push(30)
print('pop value: ',queue.pop().value)
print('pop value: ',queue.pop().value)
queue.printValue()