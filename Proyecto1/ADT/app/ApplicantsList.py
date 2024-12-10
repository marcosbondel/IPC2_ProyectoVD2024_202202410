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