class DisciplineCtrl:

    def __init__(self, repoDiscipline):
        self.__repoDiscipline = repoDiscipline
    def addDiscipline(self, discipline):
        self.__repoDiscipline.addD(discipline)
    def getAll(self):
        return self.__repoDiscipline.getAllD()
    def remove(self, id):

        self.__repoDiscipline.remove(id)
    def update(self,id,name):
        self.__repoDiscipline.update(id,name)
    def searchID(self,id):
        return self.__repoDiscipline.searchByID(id)
    def searchName(self,name):
        return self.__repoDiscipline.searchByName(name)
    def getNameById(self,id):
        return self.__repoDiscipline.getNameByID(id)
    def addCommand(self,a):
        self.__repoDiscipline.addCommand(a)
    def undo(self):
        self.__repo.undo()
        
    def redo(self):
        self.__repoDiscipline.redo()