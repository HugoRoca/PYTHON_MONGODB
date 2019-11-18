class People:

    def __init__(self, name, lastname, age, email, phone):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email
        self.phone = phone

    def json(self):
        return {
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age,
            "email": self.email,
            "phone": self.phone
        }
