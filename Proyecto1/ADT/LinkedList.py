from ADT.Node import SimpleNode

class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def len(self):
        return self.length

    def append(self, value):
        newValue = SimpleNode(value)

        if self.head is None:
            self.head = newValue
            self.length += 1
            return

        currentValue = self.head

        while currentValue.nextValue:
            currentValue = currentValue.nextValue

        currentValue.nextValue = newValue
        self.length += 1

    def printList(self):
        currentValue = self.head

        while currentValue:
            print(currentValue.value)
            currentValue = currentValue.nextValue

