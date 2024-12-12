from ADT.Node import DoublyLinkedNode

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.last = None
        self.length = 0

    def len(self):
        return self.length

    def append(self, value):
        newValue = DoublyLinkedNode(value)

        if self.head is None and self.last is None:
            self.head = newValue
            self.last = newValue
        else:
            currentValue = self.head

            while currentValue.nextValue:
                currentValue = currentValue.nextValue
                
            currentValue.nextValue = newValue
            newValue.previousValue = currentValue
            self.last = newValue

        self.length += 1

    def printListAsc(self):
        currentValue = self.head

        while currentValue is not None:
            print(currentValue)
            currentValue = currentValue.nextValue