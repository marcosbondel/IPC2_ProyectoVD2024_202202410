class SimpleNode:
    def __init__(self, value):
        self.value = value
        self.nextValue = None

class DoubleLinkedNode:

    def __init__(self, value):
        self.value = value
        self.nextValue = None
        self.previousValue = None