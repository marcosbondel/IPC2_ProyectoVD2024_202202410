from ADT.LinkedList import LinkedList

class BFigure:

    def __init__(self, bid, name):
        self.bid = bid
        self.name = name
        self.design: LinkedList = LinkedList()

    # Getter for bid
    def get_bid(self):
        return self.bid

    # Setter for bid
    def set_bid(self, bid):
        self.bid = bid

    # Getter for name
    def get_name(self):
        return self.name

    # Setter for name
    def set_name(self, name):
        self.name = name

    # Getter for design
    def get_design(self):
        return self.design

    # Setter for design
    def set_design(self, design):
        self.design = design
