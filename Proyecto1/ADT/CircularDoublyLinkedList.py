from ADT.Node import DoublyLinkedNode

class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0


    def append(self, value):
        newNode = DoublyLinkedNode(value)