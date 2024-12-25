class User:

    def __init__(self, uid, password, full_name, email, phone, address, profile):
        self.uid = uid
        self.password = password
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address
        self.profile = profile

    def __init__(self):
        pass

    @property
    def uid(self):
        return self.uid

    @uid.setter
    def uid(self, uid):
        self.uid = uid
    
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password):
        self.password = password
    
    @property
    def full_name(self):
        return self.full_name

    @full_name.setter
    def full_name(self, full_name):
        self.full_name = full_name
    
    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, email):
        self.email = email
    
    @property
    def phone(self):
        return self.phone

    @phone.setter
    def phone(self, phone):
        self.phone = phone

    @property
    def address(self):
        return self.address

    @address.setter
    def address(self, address):
        self.address = address

    @property
    def profile(self):
        return self.profile

    @profile.setter
    def profile(self, profile):
        self.profile = profile

    def is_valid(self):

        if not self.uid:
            return False

        if not self.password:
            return False

        if not self.full_name:
            return False

        if not self.email:
            return False

        if not self.phone:
            return False
    
        if not self.address:
            return False
        
        if not self.profile:
            return False

        return True