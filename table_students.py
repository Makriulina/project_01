

import sqlite3

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
sqlquery = """CREATE TABLE Studentsschool(
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
sqlquery = """INSERT INTO Studentsschool(Student_Id, Student_Name, School_Id) 
VALUES 
('201', 'Иван', 1),
('202', 'Петр', 2),
('203', 'Анастасия', 3),
('204', 'Игорь', 4);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection
  def close_connection(connection):
    
    if connection:
      connection.close()
def database_version():
        try:
          connection = get_connection()
          cursor = connection.cursor()
          cursor.execute("SELECT sqlite_version();")
          db_version = cursor.fetchone()
          print("Вы подключились к SQLite версии: ", db_version)
          close_connection(connection)
        except(Exception, sqlite3.Error) as error:
          print("Ошибка в получении данных: ", error)
          database_version()




import sqlite3
def get_connection():
    connection = sqlite3.connect('teatcher.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()
def get_student_detail(Student_Id):
  
    try:

                connection = get_connection()
                cursor = connection.cursor()
                select_query = "SELECT * FROM Studentsschool WHERE Student_Id = ?"
                cursor.execute(select_query,(Student_Id,))
                records = cursor.fetchall()
                print(records)        
    except(Exception, sqlite3.Error) as error:
                print("Ошибка в получении данных: ", error)
                get_student_detail(201)


