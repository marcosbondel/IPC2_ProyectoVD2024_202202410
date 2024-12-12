from ADT.LinkedList import LinkedList

class BFigure:

    def __init__(self, bId, name):
        self._bId = bId
        self._name = name
        self._design = LinkedList()

    def __init__(self):
        pass

    # Getter and Setter for bId
    @property
    def bId(self):
        return self._bId

    @bId.setter
    def bId(self, value):
        self._bId = value

    # Getter and Setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Getter and Setter for design
    @property
    def design(self):
        return self._design

    @design.setter
    def design(self, value):
        self._design = value