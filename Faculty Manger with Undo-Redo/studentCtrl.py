class StudentCtrl:

    def __init__(self, repo):#,validator):

        self.__repo = repo

    def addStudent(self, student):

        self.__repo.add(student)
    def getAll(self):
        return self.__repo.getAll()
    def remove(self, index):
        self.__repo.remove(index)
    def update(self,id,name):
        self.__repo.update(id,name)
    def searchID(self,id):
        return self.__repo.searchByID(id)
    def searchName(self,name):
        return self.__repo.searchByName(name)
    def getNameById(self,id):
        return self.__repo.getNameById(id)
    def writeToFile(self,fileName,student):
        self.__repo.writeToFile(fileName,student)
    def readFile(self):
        return self.__repo.readFile()
