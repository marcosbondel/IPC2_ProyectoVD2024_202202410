class Applicant:

    def __init__(self, aid, password, full_name, email, phone, address):
        self.aid = aid
        self.password = password
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address

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


    def __str__(self):
        return f'''
            aid: {self.aid}
            password: {self.password}
            full_name: {self.full_name}
            email: {self.email}
            phone: {self.phone}
            address: {self.address}
        '''