from ADT.Node import SimpleNode

class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def append(self, value):
        newNode = SimpleNode(value)

        if self.head is None and self.last is None:
            self.head = newNode
            self.last = newNode
            self.size += 1
            return

        current = self.head

        while current.nextValue:
            current = current.nextValue

        current.nextValue = newNode
        newNode.nextValue = self.head
        self.last = newNode
        self.size += 1

    def showList(self):
        current = self.head

        while current and current != self.last:
            print(current)
            current = current.nextValue
