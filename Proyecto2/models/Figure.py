class Figure:

    def __init__(self, row, column, data):
        self.row = row
        self.column = column
        self.data = data

    @property
    def row(self):
        return self.row

    @row.setter
    def row(self, value):
        self.row = value
    
    @property
    def column(self):
        return self.column

    @column.setter
    def column(self, value):
        self.column = value
   
    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, value):
        self.data = value