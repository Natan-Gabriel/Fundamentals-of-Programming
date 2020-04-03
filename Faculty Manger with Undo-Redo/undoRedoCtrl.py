class UndoRedoCtrl:

    def __init__(self, Undo):
        self.__Undo = Undo
    def addCommand(self,a,b):
        self.__Undo.addCommand(a,b)
    def undo(self):
        self.__Undo.undo()
        

    def redo(self):
        self.__Undo.redo()