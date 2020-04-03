from grade import Grade
from student import Student
from discipline import Discipline
from sort import Sort1

class GradeRepo:

    def __init__(self):

        self.__data = []
        self.__Grade=[]
        self.__Disciplines=[]
        self.__sort=Sort1(self.__data)
        #self.__controllerU=controllerU

    def add(self, grade):
        self.__data.append(grade)
    def getAll(self):

        return self.__data
    def remove(self, index):
        self.__data=[x for x in self.__data if x.getSid()!= index]
    def findById(self,id,l):
        for i in l: 
            if i.getSid()==id:
                return i
    def Average(self,id,l):
        number=0
        s=0
        for i in l:
            if i.getSid==id:
                s=s+i.getGValue
                number+=1
        find=self.GradeRepository.findById(id,l)
        if number!=0:
            find.setGValue(s/number)
        
    def greater(self,a,b):
        if a.getSname()>=b.getSname():
            return True
        else:
            return False
    def sortAlphabetically(self,id):
        
        self.__Grade=[x for x in self.__data if x.getDid()== id]
        a=Sort1(self.__Grade)
        self.__Gr=a.gnomeSort(self.greater)
        return self.__Gr
        
    def sortByMean(self,id):
        self.__Grade=[x for x in self.__data if x.getDid()== id]   # here we sort all students from a given discipline
        self.__Grade=sorted(self.__Grade,key=lambda x:x.getSid(),reverse=True ) # here we sort the students by their Id
        for i in range (0,len(self.__Grade)):

            l=[]
            appearances=1
            for j in range (i+1,len(self.__Grade)):
                if self.__Grade[j].getSid()== self.__Grade[i].getSid():
                    self.__Grade[i].setGValue(self.__Grade[j].getGValue()+self.__Grade[i].getGValue())
                    appearances+=1
            self.__Grade[i].setGValue(self.__Grade[i].getGValue()/appearances)
        l=[self.__Grade[0]]    
        for i in range (0,len(self.__Grade)-1):
            if self.__Grade[i].getSid()!=self.__Grade[i+1].getSid():
                l.append(self.__Grade[i+1])
        l=sorted(l,key=lambda x:x.getGValue(),reverse=True)
        return l
    
    def acceptance(self,x):
        if x.getGValue()<5:
            return True
    def FailAnExam(self):
        a=Sort1(self.__data)
        self.__Grade=a.filter1(self.acceptance)
        return self.__Grade

    def HighestAverage(self):
        pass
        
class GradeRepoText:
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
        self.__data=[x for x in self.__data if x.getSid() != index]
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
            if str(id) in str(student.getSid()):
                l.append(student.getSId())
        return l
    def searchByName(self,name):
        self.__data=self.getAll()
        l=[]
        for student in self.__data:
            if name.lower() in student.getSname().lower():
                l.append(student.getSname())
        return l
    def getNameById(self,id):
        self.__data=self.getAll()
        for student in self.__data:
            if student.getSid()==id:
                return student.getSname()

    def writeToFile(self,fileName,students):
        f = open(fileName, "w")
        try:
            for p in students:
                pString = str(p.getSid()) + ";" + p.getSname()+ ";" + str(p.getDid())+ ";" + p.getDname()+ ";" + str(p.getGValue()) + "\n"
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
                result.append(Grade(int(line[0]), line[1],int(line[2]),line[3],int(line[4])))
                line = f.readline().strip()
            f.close()
        except IOError as e:


            print("An error occured - " + str(e))
            raise e

        return result

import pickle
class GradeRepoBinary:
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
        self.__data=[x for x in self.__data if x.getSid() != index]
        self.writeToBinaryFile(self.__fileName,self.__data)
    def removeAll(self):
        self.writeToBianryFile([])
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
            if str(id) in str(student.getSid()):
                l.append(student.getSId())
        return l
    def searchByName(self,name):
        self.__data=self.getAll()
        l=[]
        for student in self.__data:
            if name.lower() in student.getSname().lower():
                l.append(student.getSname())
        return l
    def getNameById(self,id):
        self.__data=self.getAll()
        for student in self.__data:
            if student.getSid()==id:
                return student.getSname()
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

