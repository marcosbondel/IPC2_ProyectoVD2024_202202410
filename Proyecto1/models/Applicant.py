import re
from ADT.Pile import Pile
from ADT.DoublyLinkedList import DoublyLinkedList
from models.User import User

class Applicant(User):

    def __init__(self, aid, password, full_name, email, phone, address):
        super().__init__(aid, password, full_name, phone, email)
        self.address = address
        self.pile = Pile() 
        self.accepted_figures = DoublyLinkedList()

    def __init__(self):
        pass

    # Getter and Setter for address
    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

     # Getter and Setter for pile
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    # Getter and Setter for pile
    @property
    def pile(self):
        return self._pile

    @pile.setter
    def pile(self, value):
        self._pile = value
    
    # Getter and Setter for accepted_figures
    @property
    def accepted_figures(self):
        return self._accepted_figures

    @accepted_figures.setter
    def accepted_figures(self, value):
        self._accepted_figures = value

    def is_valid(self):
        valid_applicant = True

        if not self.is_valid_ipc_format():
            valid_applicant = False
        
        if not self.is_valid_email():
            valid_applicant = False

        if not self.is_valid_phone_number():
            valid_applicant = False

        return valid_applicant
    # Function to validate the string
    def is_valid_ipc_format(self):
        # Regular expression for "IPC-" followed by numbers
        ipc_regex = r'^IPC-\d+$'
        return re.match(ipc_regex, self.aid) is not None
    
    # Function to validate email
    def is_valid_email(self):
        # Regular expression for email validation
        email_regex =  r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ._%+-]+@[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, self.email) is not None

    # Function to validate phone number
    def is_valid_phone_number(self):
        # Regular expression for phone number validation
        phone_regex = r'^\d{8}$'
        return re.match(phone_regex, self.phone) is not None

    def __str__(self):
        return f'Id: {self.aid}\\n' \
            f'Nombre: {self.full_name}\\n' \
            f'Telefono: {self.phone}\\n' \
            f'Email: {self.email}\\n' \
            f'Direccion: {self.address}'