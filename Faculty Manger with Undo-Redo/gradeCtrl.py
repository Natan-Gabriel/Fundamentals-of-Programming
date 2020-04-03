class GradeCtrl:
    def __init__(self, repo):
        self.__repo = repo

        
    def addGrade(self, grade):
        self.__repo.add(grade)
    def getAll(self):
        return self.__repo.getAll()
    def remove(self, index):
        self.__repo.remove(index)
    def update(self,id,name):
        self.__repo.update(id,name)
    def sortAlphabetically(self,id):
        return self.__repo.sortAlphabetically(id)
    def sortByMean(self,id):
        return self.__repo.sortByMean(id)
    def FailAnExam(self):
        return self.__repo.FailAnExam()
    def HighestAverage(self):
        return self.__repo.HighestAverage