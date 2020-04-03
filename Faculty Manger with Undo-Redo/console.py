from student import Student
from discipline import Discipline
from grade import Grade
class UI:
    def __init__(self, controller,controllerD,controllerG,controllerU,controllerFile):
        self._controller = controller
        self._controllerD=controllerD
        self._controllerG=controllerG
        self._controllerU=controllerU
        self._controllerFile=controllerFile



    @staticmethod
    def printMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1 - Add student\n'
        string += '\t 2 - Add discipline\n'
        string += '\t 3 - Remove student\n'
        string += '\t 4 - Remove discipline\n'
        string += '\t 5 - Display students\n'
        string += '\t 6 - Display disciplines\n'
        string += '\t 7 - Update student\n'
        string += '\t 8 - Update discipline\n'
        string += '\t 9 - Grade students\n'
        string += '\t 10 - Search students by id\n'
        string += '\t 11 - Search students by name\n'
        string += '\t 12 - Search disciplines by id\n'
        string += '\t 13 - Search disciplines by name\n'
        string += '\t 14 - Students at a discipline, sorted alphabetically\n'
        string += '\t 15 - Students at a discipline,sorted by descending average grade\n'
        string += '\t 16 - Students who failed an exam\n'
        string += "\t 17 - undo\n"
        string += "\t 18 - redo\n"

        print(string)

    def mainMenu(self):
        keepAlive = True

        while keepAlive:
            try:
                UI.printMenu()
                command = input("Enter command: ").strip()
                if command == '0':
                    print("exit...")
                    keepAlive = False
                elif command == '1':
                    z = self.readStudent()
                    self._controller.addStudent(z)
                    self._controllerU.addCommand(["AddStudent",Student(z.getId(),z.getName())],["AddStudent",Student(z.getId(),z.getName())])
                elif command == '2':
                    z = self.ReadDiscipline()
                    self._controllerD.addDiscipline(z)
                    self._controllerU.addCommand(["AddDiscipline",Discipline(z.getId(),z.getName())],["AddDiscipline",Discipline(z.getId(),z.getName())])
                elif command == '3':
                        p = int(input("Please give an id:"))
                        name=self._controller.getNameById(p)
                        try:
                            self._controller.remove(p)
                            self._controllerU.addCommand(["removeStudent",Student(p,name)],["removeStudent",Student(p,name)])
                            self._controllerG.remove(p)
                        except Exception as ve:
                            print(ve)
                elif command == '4':
                    p = int(input("Please give an id:"))
                    name = self._controllerD.getNameById(p)
                    try:
                        self._controllerD.remove(p)
                        self._controllerU.addCommand(["removeDiscipline", Discipline(p, name)],
                                                     ["removeDiscipline", Discipline(p, name)])
                        self._controllerG.remove(p)
                    except Exception as ve:
                        print(ve)
                elif command == '5':
                    for i in self._controller.getAll():
                        print("%d %s" % (i.getId(), i.getName()))
                elif command == '6':
                    for i in self._controllerD.getAll():
                        print(i.getId(),i.getName())
                elif command=="7":
                    x=self.readStudent()#new one
                    name=self._controller.getNameById(x.getId())
                    y=Student(x.getId(),name)#old one
                    self._controller.update(x.getId(),x.getName())
                    self._controllerU.addCommand(["UpdateStudent",Student(y.getId(),y.getName())],["UpdateStudent",Student(x.getId(),x.getName())])
                elif command=="8":
                    x=self.readUpdate()
                    name=self._controllerD.getNameById(x.getId())
                    y=Discipline(x.getId(),name)
                    self._controllerD.update(x.getId(),x.getName())
                    self._controllerU.addCommand(["UpdateDiscipline",Discipline(y.getId(),y.getName())],["UpdateDiscipline",Discipline(x.getId(),x.getName())])
                elif command=="9":
                    x=UI.ReadGrade(self)
                    self._controllerG.addGrade(x)
                elif command=="10":
                    x=int(input("Id:"))
                    y=self._controller.searchID(x)
                    for i in y:
                        print(i)
                elif command=="11":
                    x=self.readName()
                    y=self._controller.searchName(x)
                    for i in y:
                        print(i)
                elif command=="12":
                    x=int(input("Id:"))
                    y=self._controllerD.searchID(x)
                    for i in y:
                        print(i)
                elif command=="13":
                    x=self.readName()
                    y=self._controllerD.searchName(x)
                    for i in y:
                        print(i)
                elif command=="14":
                    x=int(input(" Discipline Id:"))
                    y=self._controllerG.sortAlphabetically(x)
                    for i in y:
                        print(i.getSname())
                elif command=="15":
                    x=int(input("Discipline Id:"))
                    y=self._controllerG.sortByMean(x)
                    for i in y:
                        print(i.getSname(),i.getGValue())
                elif command=="16":
                    y=self._controllerG.FailAnExam()
                    for i in y:
                        print(i.getSname(),i.getGValue())
                elif command=="17":
                    self._controllerU.undo()

                elif command=="18":
                    self._controllerU.redo()
            except Exception:
                print("Invalid parameters")

    def run(self):
        while True:
            user=input(">>")
            user=user.strip()
            parts=user.split(" ")
            if user=="Exit":
                return
            elif parts[0] in self.__commands:
                try:
                    if parts[0]=="listJumper" or  parts[0]=="giveMedals" or parts[0]=="plot" :
                        self.__commands[parts[0]]()
                    else:
                        self.__commands[parts[0]](parts[1:])
                except ValueError:
                    print("Invalid numerical format")
            else:
                print("Invalid command")        
                
    def ReadGrade(self):
        x=int(input("Student id: "))
        y=int(input("Discipline id"))
        z=int(input("Give a grade"))
        
        return Grade(x,self._controller.getNameById(x),y,self._controllerD.getNameById(y),z)
       
        
        
    def readUpdate(self):
        r = int(input("Id for discipline to be change: "))
        i = input("New discipline: ")
        return Discipline(r,i)
                   
    def readPositiveInteger(self,msg):
        """
        Reads a positive integer
        Input: -
        Output: A positive integer
        """
        result = None
        while result == None:
            try:
                result = int(input(msg))
                if result < 0:
                    raise ValueError
            except ValueError:
                print("Please input a positive integer!")
        return result
    def readStudent(self):
        
        while True:
            try:
                r = int(input("Student ID="))
                i = input("Studet name=")
                return Student(r, i)
            except ValueError:
                print("Students id and must be a number!")
        return []
    def ReadDiscipline(self):
            i=int(input("Discipline id"))
            r = input("Discipline=")
            
            return Discipline(i,r)

    def readName(self):
        x=input("Give a name")
        return x
