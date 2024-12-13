from ADT.Node import Node

class Queue:

    def __init__(self):
        self.head = None
        self.size = 0

    def len(self):
        return self.size

    def enqueue(self, value):
        newNode:Node = Node(value)

        if self.head is None:
            self.head = newNode
            self.size += 1
            return

        current = self.head

        while current.nextValue:
            current = current.nextValue

        current.nextValue = newNode
        self.size += 1

    def dequeue(self):

        if self.head is None:
            return None

        deleted = self.head.value

        self.head = self.head.nextValue
        self.size -= 1

        return deleted


    def first(self):
        return self.head
        