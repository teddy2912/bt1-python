import pandas as pd
from DAO.Student import StudentDAO
from Model.Student import Student 
from ConnectDB.DBContext import dbContext
from Utill import constant
import traceback

class StudentImplement(StudentDAO): 

    def __init__(self):
        self.connect = dbContext.connect()

    def insertStudent(student, self):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            values = (student.id, student.code, student.firstName, student.lastName, student.birthOfDate, student.math, student.physics, student.chemistry)
            cursor.execute(constant.ADD_SQL ,values)
            conn.commit()
            print("insertStudent thanh cong")
        except:
 
            traceback.print_exc()
            print("insertStudent that bai")
    
    def updateStudent(student, self):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            values = (student.firstName, student.lastName, student.birthOfDate, student.math, student.physics, student.chemistry, student.id)
            cursor.execute(constant.UPDATE_SQL, values)
            conn.commit()
            print("updateStudent thanh cong")
        except:
 
            traceback.print_exc()
            print("updateStudent that bai")
    
    def deleteStudent(student_id, self):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            values = (student_id,)
            cursor.execute(constant.DELETE_SQL, values)
            conn.commit()
            print("deleteStudent thanh cong")
        except:
 
            traceback.print_exc()
            print("deleteStudent that bai")
    
    def getList(student_id, self):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            values = (student_id,)
            cursor.execute(constant.GET_STUDENT_SQL, values)
            result = cursor.fetchone()
            if result:
                print(result)
                return Student(*result)
            else:
                return None
        except:
 
            traceback.print_exc()
    
    def showList(self):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(constant.GET_ALL_SQL)        
            results = cursor.fetchall()
            students = []
            for result in results:
                print(result)
                students.append(Student(*result));
        except:
            traceback.print_exc()
