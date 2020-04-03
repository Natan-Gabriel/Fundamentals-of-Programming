from studentRepo import StudentRepo
from student import Student



class StudentFileRepository():
    def __init__(self):
        pass
        
    def writeToFile(fileName,students):
        f = open(fileName, "w")
        try:
            for p in students:
                pString = str(p.getId()) + ";" + p.getName() + "\n"
                f.write(pString)
        except Exception as e:
            print("An error occured -" + str(e))
        f.close()
    
    def readFile():
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

        return result
