class Student:
    def __init__(self,student_id,name,age,email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email

    def display(self):
        print(
            self.student_id,
            self.name,
            self.age,
            self.email)
        