class Grade:
    def __init__(self,  Sid, Sname,Did,Dname,gValue):
        self.__Sid = Sid
        self.__Sname=Sname
        self.__Did = Did
        self.__Dname=Dname
        self.__gValue=gValue
    def getDid(self):
        return self.__Did
    def getSid(self):
        return self.__Sid
    def getSname(self):
        return self.__Sname
    def getDname(self):
        return self.__Dname
    def getGValue(self):
        return self.__gValue
    def setName(self,x):
        self.__name=x
    def setGValue(self,x):
        self.__gValue=x

    
    def __eq__(self,grade):
        if isinstance(self,int) and isinstance(grade,int):
            return self==grade
        return self.__Sid==grade.__Sid and self.__Sname==grade.__Sname and self.__Did==grade.__Did and self.__Dname==grade.__Dname and self.__gValue==grade.__gValue