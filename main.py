from models.student import Student
from services.student_services import *

while True:
    print("\n---Student Management System---")
    print("""
    1. Add Student  
    2. View Students
    3. Update Student
    4. Delete Student
    5. Search Student by ID
    6. Exit
    """)

    choice=input("Enter choice: ")
    if choice=="1":
        while True:
            student_id=int(input("NEW ID: "))
            if not search_student(student_id):
                break
            print("Student ID already exists. Please enter a different ID.")

        name=input("Name: ").title().strip()
        age=int(input("Age: "))
        email=input("Email: ").replace(" ","").lower()

        student=Student(
            student_id,
            name,
            age,
            email)
        add_student(student)
        print("Student Added")

    elif choice=="2":
        view_students()

    elif choice=="3":
        student_id=int(input("Enter Student ID to Update info:"))
        print("Student Details:",search_student(student_id))
        name=input("Name:").title()
        age=int(input("Age:"))
        email=input("Email:").replace(" ","").lower()
        student=Student(
            name,
            age,
            email,
            student_id
        )
        update_student(student)
        print("Student Updated Successfully")

    elif choice=="4":
        student_id=int(input("Enter Student ID to Delete:"))
        delete_student(student_id)
        print("Student Deleted Successfully")
    
    elif choice=="5":
        student_id=int(input("Enter Student ID to Search:"))
        student=search_student(student_id)
        if student:
            print("Student found:")
            print(student)
        else:
            print("Student not found")
    
    elif choice=="6":
        print("Exiting...")
        break
    else:
        print("Invalid choice")