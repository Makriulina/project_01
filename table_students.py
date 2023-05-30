


import sqlite3

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
sqlquery = """CREATE TABLE School(
Student_Id INTEGER NOT NULL PRIMARY KEY, 
Student_Name TEXT NOT NULL, 
School_Id INTEGER NOT NULL
);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()



import sqlite3

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
sqlquery = """INSERT INTO School(Student_Id, Student_Name, School_Id) 
VALUES 
('201', 'Иван', 1),
('202', 'Петр', 2),
('203', 'Анастасия', 3),
('204', 'Игорь', 4);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

import sqlite3

def get_student(student_id):

  connection = sqlite3.connect("teachers.db")
  cursor = connection.cursor()
  query = "SELECT * FROM School JOIN Students ON School.School_Id = Students.School_Id WHERE Students.Student_id = ?"
  cursor.execute(query,(student_id,))
  records = cursor.fetchall()
  print(records)
  for row in records:
    print()

get_student(201)
