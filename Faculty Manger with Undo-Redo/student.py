class Student:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def setName(self,x):
        self.__name=x
    def __eq__(self,stud2):
        return self.__id==stud2.__id and self.__name==stud2.__name

    def __str__(self):
        return str(self.__id)+self.__name
def writeToFile(self, students):
    f = open("fileN.txt", "w")
    try:
        for p in students:
            pString = str(p.getId()) + ";" + p.getName() + "\n"
            f.write(pString)
        f.close()
    except Exception as e:
        print("An error occured -" + str(e))
    
def readFile(self):
    result = []
    try:
        f = open("fileN.txt","r")
        line = f.readline().strip()
        while  len(line) > 0:
            line = line.split(";")
            result.append(Student(int(line[0]), line[1]))
            line = f.readline().strip()
        f.close()
    except IOError as e:
        print("An error occured - " + str(e))
        raise e

    print(result)
    
        
        