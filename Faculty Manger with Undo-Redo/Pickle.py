import pickle
from studentRepo import StudentRepo
from student import Student

class PickleClass():
    def __init__(self):
       # Repository.__init__(self)
       pass
    def writeToBinaryFile(fileName, students):
        f = open(fileName, "wb")
        pickle.dump(students, f)

        f.close()

    def readBinaryFile(fileName):
        result = []
        try:
            f = open(fileName, "rb")
            return pickle.load(f)
        except EOFError:

            return []
        except IOError as e:

            print("An error occured - " + str(e))
            raise e

        return result

    def removeAll(self):
        Repository.removeAll(self)
        self.__storeToFile()
