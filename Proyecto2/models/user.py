class User:

    def __init__(self, uid, password, full_name, email, phone, address, profile):
        self._uid = uid
        self._password = password
        self._full_name = full_name
        self._email = email
        self._phone = phone
        self._address = address
        self._profile = profile
        self._role = 'user'

    def __init__(self):
        pass

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
    
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def profile(self):
        return self._profile

    @profile.setter
    def profile(self, value):
        self._profile = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def is_valid(self):

        if not self._uid:
            return False

        if not self._password:
            return False

        if not self._full_name:
            return False

        if not self._email:
            return False

        if not self._phone:
            return False
    
        if not self._address:
            return False
        
        if not self._profile:
            return False

        return True

    def __str__(self):
        return f'Id: {self.uid}\\n' \
            f'Nombre: {self.full_name}\\n' \
            f'Contrase;a: {self.password}\\n' \
            f'Telefono: {self.phone}\\n' \
            f'Correo: {self.email}\\n'

    def to_dict(self):
        return {
            'Id': self.uid,
            'Nombre': self.full_name,
            'Correo': self.email,
            'Telefono': self.phone,
            'Direccion': self.address,
            'Perfil': self.profile
        }
    
    def __dict__(self):
        return {
            'Id': self.uid,
            'Nombre': self.full_name,
            'Correo': self.email,
            'Telefono': self.phone,
            'Direccion': self.address,
            'Perfil': self.profile
        }