class Artist:

    def __init__(self, full_name, email, skills, notes):
        self.full_name = full_name
        self.email = email
        self.skills = skills
        self.notes = notes

    def __init__(self):
        pass
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
