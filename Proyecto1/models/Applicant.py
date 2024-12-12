import re
from ADT.Pile import Pile
from models.User import User

class Applicant(User):

    def __init__(self, aid, password, full_name, email, phone, address):
        super(aid, password, full_name, phone, email)
        # self.aid = aid
        # self.password = password
        # self.full_name = full_name
        # self.email = email
        # self.phone = phone
        self.address = address
        self.pile = Pile() 

    def __init__(self):
        pass

    # Getter and Setter for aid
    def get_aid(self):
        return self.aid

    def set_aid(self, aid):
        self.aid = aid

    # Getter and Setter for password
    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    # Getter and Setter for full_name
    def get_full_name(self):
        return self.full_name

    def set_full_name(self, full_name):
        self.full_name = full_name

    # Getter and Setter for email
    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    # Getter and Setter for phone
    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    # Getter and Setter for address
    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

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
        return f'aid: {self.aid}\\n' \
            f'password: {self.password}\\n' \
            f'full_name: {self.full_name}\\n' \
            f'phone: {self.phone}\\n' \
            f'email: {self.email}\\n' \
            f'address: {self.address}\\n'