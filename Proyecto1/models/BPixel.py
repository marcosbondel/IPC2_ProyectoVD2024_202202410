class BPixel:

    def __init__(self, row, col, data):
        self.row = row
        self.col = col
        self.data = data

    # Getter for row
    def get_row(self):
        return self.row

    # Setter for row
    def set_row(self, row):
        self.row = row

    # Getter for col
    def get_col(self):
        return self.col

    # Setter for col
    def set_col(self, col):
        self.col = col

    # Getter for data
    def get_data(self):
        return self.data

    # Setter for data
    def set_data(self, data):
        self.data = data
