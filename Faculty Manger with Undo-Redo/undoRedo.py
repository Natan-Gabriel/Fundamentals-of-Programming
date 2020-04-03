from studentCtrl import StudentCtrl
from student import Student
from studentRepo import StudentRepo
from discipline import Discipline
from disciplineRepo import DisciplineRepo
from disciplineCtrl import DisciplineCtrl
from grade import Grade
from gradeRepo import GradeRepo
from gradeCtrl import GradeCtrl
from undoRedoCtrl import UndoRedoCtrl

class UndoRedo():
    def __init__(self,controller,controllerD,controllerG):
        self.__undoList=[]
        self.__redoList=[]
        self._controller = controller
        self._controllerD=controllerD
        self._controllerG=controllerG
        self.index=-1
    def addCommand(self,a,b):
        self.__undoList.append(a)
        self.__redoList.append(b)
        self.index+=1

    def undo(self):

        elem=self.__undoList[self.index]
        if elem[0]=="AddStudent":
            self._controller.remove(elem[1].getId())
        elif elem[0]=="AddDiscipline":
            self._controllerD.remove(elem[1].getId())
        elif elem[0]=="removeStudent":
            self._controller.addStudent(Student(elem[1].getId(),elem[1].getName()))
        elif elem[0]=="removeDiscipline":
            self._controllerD.addDiscipline(Discipline(elem[1].getId(),elem[1].getName()))
        elif elem[0]=="UpdateStudent":
            self._controller.update(elem[1].getId(),elem[1].getName())
        elif elem[0]=="UpdateDiscipline":
            self._controllerD.update(elem[1].getId(),elem[1].getName())
        self.index-=1

               
    def redo(self):
        self.index+=1
        elem=self.__redoList[self.index]
        if elem[0]=="AddStudent":
            self._controller.addStudent(Student(elem[1].getId(),elem[1].getName()))
        elif elem[0]=="AddDiscipline":
            self._controllerD.addDiscipline(Discipline(elem[1].getId(),elem[1].getName()))
        elif elem[0]=="removeStudent":
            self._controller.remove(elem[1].getId())
        elif elem[0]=="removeDiscipline":
            self._controllerD.remove(elem[1].getId())
        elif elem[0]=="UpdateStudent":
            self._controller.update(elem[1].getId(),elem[1].getName())
        elif elem[0]=="UpdateDiscipline":
            self._controllerD.update(elem[1].getId(),elem[1].getName())

    def getAllUndo(self):
        return self.__undoList


