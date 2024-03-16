import psycopg2


#replace with your db information
DB_NAME = "ENTER NAME HERE"
DB_USER = "ENTER USER HERE"
DB_PASS = "ENTER PASSWORD HERE"
DB_HOST = "ENTER HOST HERE"
DB_PORT = "ENTER PORT HERE"




#displays students
def getAllStudents() :
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for data in rows:
        print("Id: " + str(data[0]) + " First Name: " + data[1] + " Last Name: " + data[2] + " Email: " + data[3] + " Enrollment Date: " + str(data[4]))
    
    cur.close()
    conn.close()

#adds a student
def addStudent(first_name, last_name, email, enrollment_date):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{}', '{}', '{}', '{}')".format(first_name, last_name, email, enrollment_date))


    conn.commit()
    cur.close()
    conn.close()

#updates a students email
def updateStudentEmail(student_id, new_email):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = \'{}\' WHERE student_id = {}".format(new_email, student_id))
    
    conn.commit()
    cur.close()
    conn.close()

#deletes a student
def deleteStudent(student_id):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = {}".format(student_id))
    
    conn.commit()
    cur.close()
    conn.close()

#loop through till the user says something other than add update delete or display
while(True):
    var = input("what would you like to do (add, update, delete, display): ")
    if var == "add":
         fn = input("First Name: ")
         ln = input("Last Name: ")
         em = input("Email: ")
         date = input("Enrollment date (yyyy-mm-dd): ")
         addStudent(fn,ln,em,date)
    elif var == "update":
         id = input("Enter Id of student to update: ")
         em = input("Enter new email: " )
         updateStudentEmail(id, em)
    elif var == "delete":
        id = input("Enter Id to delete: ")
        deleteStudent(id)
    elif var == "display":
        getAllStudents()
    else:
        break