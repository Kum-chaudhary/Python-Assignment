from Connection import get_connection
import os

def add_student():
    conn = get_connection()

    cursor = conn.cursor()

    name = input("Enter student name: ")
    class_name = input("Enter class name: ")
    monthly_fees = input("Enter your monthly fees : ")

    cursor.execute("INSERT INTO STUDENTS (NAME, CLASS_NAME, MONTHLY_FEE) VALUES (%s,%s,%s)",(name,class_name,monthly_fees))

    conn.commit()
    print("sucessfully added new records !")

def ViewALL_student():
    conn = get_connection()

    cursor = conn.cursor()

    query = "SELECT * FROM STUDENTS"

    cursor.execute(query)
    conn.commit()

    records = cursor.fetchall()

    for student in records:
        # print student
        print(f"ID : {student[0]}")
        print(f"Name : {student[1]}")
        print(f"Class_name : {student[2]}")
        print(f"Monthly_fees : {student[3]}")
        print("-------------------------------")


def search_class():
    conn = get_connection()
    cursor = conn.cursor()

    class_name = input("Enter your class name: ")
    cursor.execute("SELECT * FROM STUDENTS WHERE CLASS_NAME = %s",(class_name,))

    results = cursor.fetchall()

    print(results)

def update_fees():
    conn = get_connection()
    cursor = conn.cursor()

    id = int(input("Enter your id :"))
    Monthly_fees = input("Enter your fees :")

    query = "UPDATE STUDENTS SET MONTHLY_FEE = %s WHERE ID = %s"
    values = (Monthly_fees,id)

    cursor.execute(query,values)
    conn.commit()

    if cursor.rowcount > 0:
        print("Sucessfully records updated !")
    else:
        print("ERROR : No record found with the given id !")


def del_student():
    conn = get_connection()
    cursor = conn.cursor()

    student_id = int(input("Enter id : "))

    cursor.execute("DELETE FROM STUDENTS WHERE ID = %s",(student_id,))

    if cursor.rowcount >= 1:
        print("Sucessfully deleted !!!")
    else:
        print("Something went wrong !")
    conn.commit()


menu = """
        TUITION FEES MANAGEMENT 
        1.ADD STUDENT
        2.VIEW ALL STUDENT
        3.SEARCH BY CLASS
        4.UPDATE FEES
        5.DELETE STUDENT
        6.EXIT
"""    

status = True
while status:
    print(menu)

    choice = int(input("Enter your choice:"))

    if choice == 1:
        add_student()
    elif choice == 2:
        ViewALL_student()
    elif choice == 3:
        search_class()
    elif choice == 4:
        update_fees()    
    elif choice == 5:
        del_student()
    else:
        print("invalid choice")


