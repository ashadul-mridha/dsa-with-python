class Stack:
    def __init__(self, value):
        self.values=[value]
        self.height = 1


    def push(self, value):
        try:
            # raise Exception('Push Failed')
            insertNewData = self.values.append(value)
            self.height += 1
            return insertNewData
        except Exception as e:
            print("Error", e)


    def pop(self):
        try:
            removeName = self.values.pop()
            self.height -= 1
            return removeName
        except Exception as e:
            print('Error on pop', e)


    def printStack(self):
        try:
            return self.values
        except Exception as e:
            print('Error on print stack', e)

myName = Stack('Ashadul')
myName.push('sani')
myName.push('Sourav')
print('pop', myName.pop())

print(myName.printStack())