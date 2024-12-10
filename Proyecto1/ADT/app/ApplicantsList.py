from ADT.LinkedList import LinkedList
from models.Applicant import Applicant

class ApplicantsList(LinkedList):

    def __init__(self):
        super().__init__()

    def printList(self):
        currentValue: Applicant = self.head

        while currentValue is not None:
            print(currentValue.value)
            currentValue = currentValue.nextValue