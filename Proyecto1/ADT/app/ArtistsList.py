from ADT.LinkedList import LinkedList
from models.Artist import Artist

class ArtistsList(LinkedList):

    def __init__(self):
        super().__init__()

    def printListAsc(self):
        currentValue: Artist = self.head

        while currentValue is not None:
            print(currentValue.value)
            currentValue = currentValue.nextValue


    def findByID(self, id):
        currentValue: Artist = self.head

        while currentValue.nextValue:
            if currentValue.get_aid() == id:
                return currentValue
            curentValue = currentValue.nextValue