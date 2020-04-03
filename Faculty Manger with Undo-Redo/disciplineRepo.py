from discipline import Discipline
from student import Student


class DisciplineRepo:

    def __init__(self):
        self.__dataDiscipline = []

    def addD(self, discipline):

        self.__dataDiscipline.append(discipline)
    def getAllD(self):

        return self.__dataDiscipline
    def remove(self, id):
        self.__dataDiscipline=[x for x in self.__dataDiscipline if x.getId() != id]
    def update(self,id,name):
        for i in self.__dataDiscipline:
            if i.getId()==id:
                i.setName(name)
                return
    def searchByID(self,id):
        l=[]
        for disciplines in self.__dataDiscipline:
            if str(id) in str(disciplines.getId()):
                l.append(disciplines.getId())
        return l
    def searchByName(self,name):
        l=[]
        for discipline in self.__dataDiscipline:
            if name.lower() in discipline.getName().lower():
                l.append(discipline.getName())
        return l
    def getNameByID(self,id):
        for dis in self.__dataDiscipline:
            if dis.getId()==id:
                return dis.getName()
            
    
    

class DisciplineRepoText:
    def __init__(self,fileName):

        self.__data = []
        self.__fileName=fileName
        
    def addD(self, student):

        self.__data=self.getAllD()
        self.__data.append(student)
        self.writeToFile(self.__fileName,self.__data)
    def getAllD(self):
        return self.readFile()
    def remove(self, index):

        self.__data=self.getAllD()
        self.__data=[x for x in self.__data if x.getId() != index]
        self.writeToFile(self.__fileName,self.__data)
    def removeAll(self):
        self.writeToFile(self.__fileName,[])
    def store(self,student):
        self.__data.append(student)
        
    def update(self,id,name):
        self.__data=self.getAllD()
        index=0
        for i in self.__data:
            if i.getId()==id:
                i.setName(name)
        self.writeToFile(self.__fileName,self.__data)
    def searchByID(self,id):
        self.__data=self.getAllD()
        l=[]
        for student in self.__data:
            if str(id) in str(student.getId()):
                l.append(student.getId())
        return l
    def searchByName(self,name):
        self.__data=self.getAllD()
        l=[]
        for student in self.__data:
            if name.lower() in student.getName().lower():
                l.append(student.getName())
        return l
    def getNameByID(self,id):
        self.__data=self.getAllD()
        for student in self.__data:
            if student.getId()==id:
                return student.getName()
    def find(self,id):
        self.__data=self.getAllD()
        for student in self.__data:
            if student.getId()==id:
                return Student(id,student.getName())
    def writeToFile(self,fileName,students):
        f = open(fileName, "w")
        try:
            for p in students:
                pString = str(p.getId()) + ";" + p.getName() + "\n"
                f.write(pString)
        except Exception as e:
            print("An error occured -" + str(e))
        f.close()
    
    def readFile(self):
        result = []
        try:
            f = open(self.__fileName,"r")
            line = f.readline().strip()
            while  len(line) > 0:
                line = line.split(";")
                result.append(Discipline(int(line[0]), line[1]))
                line = f.readline().strip()
            f.close()
        except IOError as e:


            print("An error occured - " + str(e))
            raise e

        return result       
            
import pickle
class DisciplineRepoBinary:
    def __init__(self,fileName):

        self.__data = []
        self.__fileName=fileName
        
    def addD(self, student):

        self.__data=self.getAllD()
        self.__data.append(student)
        self.writeToBinaryFile(self.__data)
    def getAllD(self):
        
        return self.readBinaryFile()
    def remove(self, index):
        self.__data=self.getAllD()
        self.__data=[x for x in self.__data if x.getId() != index]
        self.writeToBinaryFile(self.__data)
    def removeAll(self):
        self.writeToFile([])
    def store(self,student):
        self.__data.append(student)
        
    def update(self,id,name):
        self.__data=self.getAllD()
        index=0
        for i in self.__data:
            if i.getId()==id:
                i.setName(name)
        self.writeToBinaryFile(self.__data)
    def searchByID(self,id):
        self.__data=self.getAllD()
        l=[]
        for student in self.__data:
            if str(id) in str(student.getId()):
                l.append(student.getId())
        return l
    def searchByName(self,name):
        self.__data=self.getAllD()
        l=[]
        for student in self.__data:
            if name.lower() in student.getName().lower():
                l.append(student.getName())
        return l
    def getNameByID(self,id):
        self.__data=self.getAllD()
        for student in self.__data:
            if student.getId()==id:
                return student.getName()
    def find(self,id):
        self.__data=self.getAllD()
        for student in self.__data:
            if student.getId()==id:
                return Student(id,student.getName())
    def writeToBinaryFile(self, persons):
        f = open(self.__fileName, "wb")
        pickle.dump(persons, f)
        f.close()
    
    def readBinaryFile(self):
        result = []
        try:
            f = open(self.__fileName, "rb")
            return pickle.load(f)
        except EOFError:
            return []
        except IOError as e:
            print("An error occured - " + str(e))
            raise e
    
        return result

