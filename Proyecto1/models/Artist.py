import re

class Artist:

    def __init__(self, aid, password, full_name, phone, email, skills, notes):
        self.aid = aid
        self.password = password
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.skills = skills
        self.notes = notes

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
    
    # Getter and Setter for phone
    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    # Getter and Setter for email
    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

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
            valid_artist = False
        
        if not self.is_valid_email():
            valid_artist = False

        if not self.is_valid_phone_number():
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
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, self.email) is not None

    # Function to validate phone number
    def is_valid_phone_number(self):
        # Regular expression for phone number validation
        phone_regex = r'^\d{8}$'
        return re.match(phone_regex, self.phone) is not None

    def __str__(self):
        return f'''
            aid: {self.aid}
            password: {self.password}
            full_name: {self.full_name}
            phone: {self.phone}
            email: {self.email}
            skills: {self.skills}
            notes: {self.notes}
        '''
