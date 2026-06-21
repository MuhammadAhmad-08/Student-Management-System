from models.student import student
from services.student_services import *

while True:
    print("\n---Student Management System---")
    print("""
    1. Add Student  
    2. View Students  
    3. Exit
    """)

    choice=input("Enter choice: ")
    if choice=="1":
        name=input("Name: ")
        age=int(input("Age: "))
        email=input("Email: ")

        student=student(
            name,
            age,
            email)
        add_student(student)
        print("Student Added")

    elif choice=="2":
        view_students()


    elif choice=="3":
        break
    else:
        print("Invalid choice")