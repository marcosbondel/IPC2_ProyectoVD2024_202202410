from ADT.Node import NodePile

class Pile:

    def __init__(self):
        self.peek = None
        self.size = 0

    def len(self):
        return self.size

    def push(self, value):
        newNode = NodePile(value)

        newNode.down = self.peek
        self.peek = newNode

        self.size += 1

    def pop(self):

        if self.peek is None: 
            return None

        node_to_delete = self.peek

        self.peek = self.peek.down

        self.size -= 1

        return node_to_delete

    def peek(self):
        return self.peek
        