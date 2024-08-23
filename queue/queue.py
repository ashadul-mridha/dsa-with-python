class Queue:
    def __init__(self, value):
        try:
            self.values = [value]
            self.length = 1
        except Exception as e:
            print('Class Init error: ', e)

    def inQueue(self, value):
        try:
            self.values.append(value)
            self.length += 1
        except Exception as e: 
            print('InQueue:', e)

    def deQueue(self):
        try:
            pop_value = self.values.pop(0)
            self.length -= 1
            return pop_value
        except Exception as e:
            print('DeQueue:', e)


    def printValue(self):
        try:
            return self.values
        except Exception as e:
            print('Exception', e)


queue = Queue(10)
queue.inQueue(15)
queue.inQueue(20)
queue.deQueue()

print(queue.printValue())