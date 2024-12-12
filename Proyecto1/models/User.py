class User:

    def __init__(self, aid, password, full_name, phone, email):
        self._aid = aid
        self._password = password
        self._full_name = full_name
        self._phone = phone
        self._email = email

    # Getter and Setter for aid
    @property
    def aid(self):
        return self._aid

    @aid.setter
    def aid(self, value):
        self._aid = value

    # Getter and Setter for password
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    # Getter and Setter for full_name
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value

    # Getter and Setter for phone
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    # Getter and Setter for email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    # Optional: Add __str__ for better representation
    def __str__(self):
        return f"User(aid={self._aid}, full_name={self._full_name}, email={self._email})"
