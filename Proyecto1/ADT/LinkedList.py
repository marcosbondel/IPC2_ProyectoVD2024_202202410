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
            return

        currentValue = self.head

        while currentValue.nextValue is not None:
            currentValue = currentValue.nextValue

        currentValue.nextValue = newValue

    def printList(self):
        currentValue = self.head

        while currentValue is not None:
            print(currentValue.value)
            currentValue = currentValue.nextValue

