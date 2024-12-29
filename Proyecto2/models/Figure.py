from models.Pixel import Pixel

class Figure:

    def __init__(self, fid, name, uid, edited = False):
        self._fid = fid
        self._name = name
        self._uid = _uid
        self._edited = False
        self._design = []
        self._matrix = None

    def __init__(self):
        pass

    # Getter and Setter for fid
    @property
    def fid(self):
        return self._fid

    @fid.setter
    def fid(self, value):
        self._fid = value

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

    # Getter and Setter for edited
    @property
    def edited(self):
        return self._edited

    @edited.setter
    def edited(self, value):
        self._edited = value

    # Getter and Setter for User
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value

    # Getter and Setter for the Matrix
    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = value

    def to_dict(self):
        return {
            'fid': self.fid,
            'uid': self.uid,
            'name': self.name,
            'matrix': self.matrix,
            'edited': 'Editado' if self.edited else ''
        }

    # def __str__(self):
    #     return f'''
    #         fid: {self.fid},
    #         uid: {self.uid},
    #         name: {self.name}
    #     '''
