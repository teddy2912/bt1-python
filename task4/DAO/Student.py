from abc import ABC,abstractmethod
from Model.Student import Student

class StudentDAO(ABC):
    @abstractmethod
    def importData():
        pass
    @abstractmethod
    def insertStudent(student : Student):
        pass
    @abstractmethod
    def updateStudent(student : Student):
        pass
    @abstractmethod
    def deleteStudent(student : Student):
        pass
    @abstractmethod
    def showList(student : Student):
        pass