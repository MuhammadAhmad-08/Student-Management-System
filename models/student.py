class student:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

    def display(self):
        print(
            self.name,
            self.age,
            self.email)
        