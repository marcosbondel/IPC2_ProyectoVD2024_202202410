from models.user import User

class Applicant(User):

    def __init__(self, uid, password, full_name, email, phone, address, profile):
        super().__init__(uid, password, full_name, email, phone, address, profile)

    def __init__(self):
        pass
