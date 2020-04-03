class cFile:

    def __init__(self,file):

        self.__file = file

    def store(self, st):
        self.__file.store(st)

    def update(self, id, st):
        self.__file.update(id,st)


    def remove(self, id):
        self.__file.remove(id)

    
    def __storeToFile(self):
        self.__file.__storeToFile()
    
    def removeAll(self):
        self.__file.removeAll()
    def writeToFile(self,students):
        self.__file.writeToFile([students])
    def readFile(self):
        self.__file.readFile()
class cPickle:
    pass