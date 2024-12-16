import re
from models.User import User
from ADT.CircularLinkedList import CircularLinkedList

class Artist(User):

    def __init__(self, aid, password, full_name, phone, email, skills, notes):
        super().__init__(aid, password, full_name, phone, email)
        self.skills = skills
        self.notes = notes
        self.accepted_figures = CircularLinkedList()

    def __init__(self):
        pass

    @property
    def skills(self):
        return self._skills

    @skills.setter
    def skills(self, value):
        self._skills = value
    
    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, value):
        self._notes = value
 
    @property
    def accepted_figures(self):
        return self._accepted_figures

    @accepted_figures.setter
    def accepted_figures(self, value):
        self._accepted_figures = value


    def is_valid(self):
        valid_artist = True

        if not self.is_valid_ipc_format():
            print("No valid id")
            valid_artist = False
        
        if not self.is_valid_email():
            print("No valid email")
            valid_artist = False

        if not self.is_valid_phone_number():
            print("No valid phone")
            valid_artist = False

        return valid_artist
    # Function to validate the string
    def is_valid_ipc_format(self):
        # Regular expression for "IPC-" followed by numbers
        ipc_regex = r'^ART-\d+$'
        return re.match(ipc_regex, self.aid) is not None
    
    # Function to validate email
    def is_valid_email(self):
        # Regular expression for email validation
        email_regex = r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ._%+-]+@[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, self.email) is not None

    # Function to validate phone number
    def is_valid_phone_number(self):
        # phone_regex = r'^\d{8}$'
        phone_regex = r'^\d{9}$'
        return re.match(phone_regex, self.phone) is not None

    def __str__(self):
        return f'Id: {self.aid}\\n' \
            f'Nombre: {self.full_name}\\n' \
            f'Telefono: {self.phone}\\n' \
            f'Email: {self.email}\\n' \
            f'Habilidades: {self.skills}\\n' \
            f'Notas: {self.notes}'
