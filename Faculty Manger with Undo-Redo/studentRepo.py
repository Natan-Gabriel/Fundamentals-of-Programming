from student import Student


class StudentRepo:

    def __init__(self):

        self.__data = []

        
    def add(self, student):

        self.__data.append(student)
    def getAll(self):

        return self.__data
    def remove(self, index):
        self.__data=[x for x in self.__data if x.getId() != index]
    def removeAll(self):
        self.__data=[]
    def store(self,student):
        self.__data.append(student)
        
    def update(self,id,name):
        index=0
        for i in self.__data:
            if i.getId()==id:
                i.setName(name)
    def searchByID(self,id):
        l=[]
        for student in self.__data:
            if str(id) in str(student.getId()):
                l.append(student.getId())
        return l
    def searchByName(self,name):
        l=[]
        for student in self.__data:
            if name.lower() in student.getName().lower():
                l.append(student.getName())
        return l
    def getNameById(self,id):
        for student in self.__data:
            if student.getId()==id:
                return student.getName()
    def find(self,id):
        for student in self.__data:
            if student.getId()==id:
                return Student(id,student.getName())

class StudentRepoText:
    def __init__(self,fileName):

        self.__data = []
        self.__fileName=fileName
        
    def add(self, student):

        self.__data=self.getAll()
        self.__data.append(student)
        self.writeToFile(self.__fileName,self.__data)
    def getAll(self):
        return self.readFile()
    def remove(self, index):

        self.__data=self.getAll()
        self.__data=[x for x in self.__data if x.getId() != index]
        self.writeToFile(self.__fileName,self.__data)
    def removeAll(self):
        self.writeToFile(self.__fileName,[])
    def store(self,student):
        self.__data.append(student)
        
    def update(self,id,name):
        self.__data=self.getAll()
        index=0
        for i in self.__data:
            if i.getId()==id:
                i.setName(name)
        self.writeToFile(self.__fileName,self.__data)
    def searchByID(self,id):
        self.__data=self.getAll()
        l=[]
        for student in self.__data:
            if str(id) in str(student.getId()):
                l.append(student.getId())
        return l
    def searchByName(self,name):
        self.__data=self.getAll()
        l=[]
        for student in self.__data:
            if name.lower() in student.getName().lower():
                l.append(student.getName())
        return l
    def getNameById(self,id):
        self.__data=self.getAll()
        for student in self.__data:
            if student.getId()==id:
                return student.getName()
    def find(self,id):
        self.__data=self.getAll()
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
                result.append(Student(int(line[0]), line[1]))
                line = f.readline().strip()
            f.close()
        except IOError as e:

            print("An error occured - " + str(e))
            raise e

        return result
import pickle
class StudentRepoBinary:
    def __init__(self,fileName):

        self.__data = []
        self.__fileName=fileName
        
    def add(self, student):

        self.__data=self.getAll()
        self.__data.append(student)
        self.writeToBinaryFile(self.__data)
    def getAll(self):
        return self.readBinaryFile()
    def remove(self, index):

        self.__data=self.getAll()
        self.__data=[x for x in self.__data if x.getId() != index]
        self.writeToBinaryFile(self.__data)
    def removeAll(self):
        self.writeToBinaryFile([])
    def store(self,student):
        self.__data.append(student)
        
    def update(self,id,name):
        self.__data=self.getAll()
        index=0
        for i in self.__data:
            if i.getId()==id:
                i.setName(name)
        self.writeToBinaryFile(self.__data)
    def searchByID(self,id):
        self.__data=self.getAll()
        l=[]
        for student in self.__data:
            if str(id) in str(student.getId()):
                l.append(student.getId())
        return l
    def searchByName(self,name):
        self.__data=self.getAll()
        l=[]
        for student in self.__data:
            if name.lower() in student.getName().lower():
                l.append(student.getName())
        return l
    def getNameById(self,id):
        self.__data=self.getAll()
        for student in self.__data:
            if student.getId()==id:
                return student.getName()
    def find(self,id):
        self.__data=self.getAll()
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
