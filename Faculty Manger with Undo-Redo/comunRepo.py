import gradeRepo
import student
import studentRepo
from grade import Grade
class SortingRepository:

    def __init__(self):

        self.__data = []
        self.__Grade=[]

    def add(self, grade):

        self.__data.append(grade)
    def getAll(self):

        return self.__data
    def remove(self, index):

        self.__data=[x for x in self.__data if x.getSid()!= index]
        
    def update(self,id,name):
        for i in self.__data:
            if i.getId()==id:
                i.setName(name)
    def sortAlphabetically(self,id):
        self.__Grade=[x for x in self.__data if x.getDid()== id]
        sorted(self.__Grade, key=lambda Student: Student.getName())
        return self.__Grade
