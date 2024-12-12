class SimpleNode:
    def __init__(self, value):
        self.value = value
        self.nextValue = None

class DoublyLinkedNode:

    def __init__(self, value):
        self.value = value
        self.nextValue = None
        self.previousValue = None

class NodePile:

    def __init__(self, value):
        self.value = value
        self.down = None