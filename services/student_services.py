from database.db import connect



def add_student(student):
    conn=connect()
    cursor=conn.cursor()

    query="""
    INSERT INTO students
    (name,age,email)
    VALUES(%s,%s,%s)"""


    cursor.execute(
        query,
        (student.name,
        student.age,
        student.email))
    conn.commit()
    cursor.close()
    conn.close()

def view_students():
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students")

    students=cursor.fetchall()

    for s in students:
        print(s)
    cursor.close()
    conn.close()
