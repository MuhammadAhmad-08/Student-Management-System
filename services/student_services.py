from database.db import connect
from models.student import Student


def add_student(Student):
    conn=connect()
    cursor=conn.cursor()

    query="""
    INSERT INTO students(student_id,name,age,email)
    VALUES(%s,%s,%s,%s)"""

    cursor.execute(
        query,
        (Student.student_id,
        Student.name,
        Student.age,
        Student.email))
    conn.commit()
    cursor.close()
    conn.close()

def view_students():
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students")
    cursor.execute("SELECT * FROM students ORDER BY student_id ASC")

    students=cursor.fetchall()

    for s in students:
        print(s)
    cursor.close()
    conn.close()

def delete_student(student_id):
    conn=connect()
    cursor=conn.cursor()

    query="DELETE FROM students where student_id=%s"
    cursor.execute(query,(student_id,))
    conn.commit()
    cursor.close()
    conn.close()

def update_student(Student):
    conn=connect()
    cursor=conn.cursor()

    query="""
    UPDATE students
    SET name=%s, age=%s, email=%s
    WHERE student_id=%s"""

    cursor.execute(query,
                   (Student.student_id,
                    Student.name,
                    Student.age,
                    Student.email))
    conn.commit()
    cursor.close()
    conn.close()

def search_student(student_id):
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_id=%s",(student_id,))
    student=cursor.fetchone()
    cursor.close()
    conn.close()
    return student