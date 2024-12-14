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

    # Getter and Setter for skills
    def get_skills(self):
        return self.skills

    def set_skills(self, skills):
        self.skills = skills

    # Getter and Setter for notes
    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes

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
        return f'aid: {self.aid}\\n' \
            f'password: {self.password}\\n' \
            f'full_name: {self.full_name}\\n' \
            f'phone: {self.phone}\\n' \
            f'email: {self.email}\\n' \
            f'skills: {self.skills}\\n' \
            f'notes: {self.notes}'
