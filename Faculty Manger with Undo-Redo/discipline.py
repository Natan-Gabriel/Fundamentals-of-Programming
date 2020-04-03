class Discipline:

    def __init__(self, id,name):

        self.__id=id
        self.__name = name
    def getName(self):
        return self.__name
    def getId(self):
        return self.__id
    def setName(self,x):
        self.__name=x 
    def __eq__(self,discipline):
        return self.__id==discipline.getId() and self.__name==discipline.Name()

    @property
    def __str__(self):
        return str(self.__id)+self.__name