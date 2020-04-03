from studentCtrl import StudentCtrl
from student import Student
from studentRepo import StudentRepo,StudentRepoText,StudentRepoBinary
from discipline import Discipline
from disciplineRepo import DisciplineRepo,DisciplineRepoText,DisciplineRepoBinary
from disciplineCtrl import DisciplineCtrl
from grade import Grade
from gradeRepo import GradeRepo,GradeRepoText,GradeRepoBinary
from gradeCtrl import GradeCtrl
from undoRedo import UndoRedo
from undoRedoCtrl import UndoRedoCtrl
from ControllerFile import cFile
from File import StudentFileRepository
from console import UI

result = []
try:
    f = open("settings.properties","r")
    line = f.readline().strip()
    while  len(line) > 0:
        line = line.split("=")
        result.append([line[0], line[1]])
        line = f.readline().strip()
    f.close()
except IOError as e:
    print("An error occured - " + str(e))
    raise e


print("Selected repository:",result[0][1].strip())
if result[0][1].strip()=='inmemory':
    repo = StudentRepo()
    disciplineRepo=DisciplineRepo()
    gradeRepo=GradeRepo()
elif result[0][1].strip()=='textfiles':
    f=open(result[1][1].strip(),'a+')
    f.close()
    f=open(result[2][1].strip(),'a+')
    f.close()
    f=open(result[3][1].strip(),'a+')
    f.close()
    repo = StudentRepoText(result[1][1].strip())
    disciplineRepo=DisciplineRepoText(result[2][1].strip())
    gradeRepo=GradeRepoText(result[3][1].strip())
elif result[0][1].strip()=='binaryfiles':
    f=open(result[1][1].strip(),'a+b')
    f.close()
    f=open(result[2][1].strip(),'a+b')
    f.close()
    f=open(result[3][1].strip(),'a+b')
    f.close()
    
    repo = StudentRepoBinary(result[1][1].strip())
    disciplineRepo=DisciplineRepoBinary(result[2][1].strip())
    gradeRepo=GradeRepoBinary(result[3][1].strip())
else:
    print("Invalid text in settings.properties")


studentCtrl = StudentCtrl(repo)

studentCtrl.addStudent(Student(1, "eminescu"))
studentCtrl.addStudent(Student(2, "enescu"))
studentCtrl.addStudent(Student(3, "badita"))
studentCtrl.addStudent(Student(111, "gangos"))

#
disciplineCtrl=DisciplineCtrl(disciplineRepo)

disciplineCtrl.addDiscipline(Discipline(2, "maths"))
disciplineCtrl.addDiscipline(Discipline(1, "english"))
disciplineCtrl.addDiscipline(Discipline(3, "physics education"))
disciplineCtrl.addDiscipline(Discipline(11, "computer science"))

#

gradeCtrl=GradeCtrl(gradeRepo)

gradeCtrl.addGrade(Grade(1,"Ana",1,"maths",3))
gradeCtrl.addGrade(Grade(10,"Tini",2,"maths",8))
gradeCtrl.addGrade(Grade(11,"Toni",2,"maths",6))
gradeCtrl.addGrade(Grade(3,"Ion",1,"english",2))
gradeCtrl.addGrade(Grade(2,"Gigi",1,"english",7.5))
gradeCtrl.addGrade(Grade(4,"Mihnea",1,"english",8))
gradeCtrl.addGrade(Grade(5,"Gheorghe",1,"english",9))
gradeCtrl.addGrade(Grade(6,"Hagi",1,"english",6))
gradeCtrl.addGrade(Grade(7,"Urko",1,"english",9))
gradeCtrl.addGrade(Grade(8,"Bastos",1,"english",10))
gradeCtrl.addGrade(Grade(5,"Gheorghe",1,"english",8))
gradeCtrl.addGrade(Grade(6,"Hagi",1,"english",7))
gradeCtrl.addGrade(Grade(7,"Urko",1,"english",9))
gradeCtrl.addGrade(Grade(8,"Bastos",1,"english",10))

undoRedo=UndoRedo(studentCtrl,disciplineCtrl,gradeCtrl)
undoRedoCtrl=UndoRedoCtrl(undoRedo)

file=StudentFileRepository()
controllerFile=cFile(file)

ui=UI(studentCtrl,disciplineCtrl,gradeCtrl,undoRedoCtrl,controllerFile)
ui.mainMenu()
