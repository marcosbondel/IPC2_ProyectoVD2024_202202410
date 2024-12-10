from ADT.DoublyLinkedList import DoublyLinkedList
from models.Applicant import Applicant

class ApplicantsList(DoublyLinkedList):

    def __init__(self):
        super().__init__()

    def printListAsc(self):
        currentValue: Applicant = self.head

        while currentValue is not None:
            print(currentValue.value)
            currentValue = currentValue.nextValue

    def findByID(self, id):
        currentValue: Applicant = self.head

        while currentValue is not None:
            if currentValue.value.get_aid() == id:
                return currentValue
            curentValue = currentValue.nextValue