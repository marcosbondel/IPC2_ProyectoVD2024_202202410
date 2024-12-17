from ADT.LinkedList import LinkedList

class BFigure:

    def __init__(self, bId, name):
        self._bId = bId
        self._name = name
        self._applicant = ''
        self._artist = ''
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

    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        self._applicant = value

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, value):
        self._artist = value

    # Getter and Setter for design
    @property
    def design(self):
        return self._design

    @design.setter
    def design(self, value):
        self._design = value

    def showInfoInArtistArea(self):
        return f'Figura: {self.name}\n Solicitante: {self.applicant.aid} - {self.applicant.full_name}'

    def __str__(self):
        return f'bId: {self.bId}\\n' \
            f'name: {self.name}\\n' \
            f'name: {self.applicant.full_name}\\n'

        # return f'Id: {self.bId}\n Nombre: {self.name}\n Solicitante: {self.applicant.full_name}'
