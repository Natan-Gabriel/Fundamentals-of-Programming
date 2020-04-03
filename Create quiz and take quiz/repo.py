from random import randint
class Repo:
    def __init__(self,id=0,text=0,a=0,b=0,c=0,correct=0,diff=0):
        self.__id=id
        self.__text=text
        self.__a=a
        self.__b=b
        self.__c=c
        self.__correct=correct
        self.__diff=diff
        

    def get_id(self):
        return self.__id


    def get_text(self):
        return self.__text


    def get_a(self):
        return self.__a


    def get_b(self):
        return self.__b


    def get_c(self):
        return self.__c


    def get_correct(self):
        return self.__correct


    def get_diff(self):
        return self.__diff


    def set_id(self, value):
        self.__id = value


    def set_text(self, value):
        self.__text = value


    def set_a(self, value):
        self.__a = value


    def set_b(self, value):
        self.__b = value


    def set_c(self, value):
        self.__c = value


    def set_correct(self, value):
        self.__correct = value


    def set_diff(self, value):
        self.__diff = value

    def add(self,parts,a,filename):
        '''
        input-7 parameters reveived form ui
        outpu-write to the master.txt file the 
        corresponding question
        '''
        f=open(filename,'a')
        try:
            if filename=='master.txt':
                f.write('\n')
            f.write(str(a))
            for  i in parts[1:]:
                f.write(';')
                f.write(str(i))
            if filename!='master.txt':
            
                f.write('\n')
            f.close()    
        except Exception as e:
            print(e)
            
    def read(self,filename):
        '''
        this function read a filename
        line buy line and return in 
        contstant list the reasult 
        of reading
        input-filename
        '''
        result=[]
        try:   
            f=open(filename,'r')
            line=f.readline().strip()
            while len(line)>0:
                line=line.split(';')
                result.append([line[0],line[1],line[2],line[3],line[4],line[5],line[6]])
                line=f.readline().strip()
            f.close()
        except IOError as e:
            print(e)
        return result
    def create(self,parts):
        '''
        input;pats
        this function creates a quiz 
        on a given difficulty
        with a given number of questions
        and this quiz will be stored in 
        a file specifed in parts
        '''
        list=[]
        diff=parts[1]
        #try:
        number=int(parts[2])
        #except ValueError('Enter a integer!!')
        filename=parts[3]
        result=self.read('master.txt')

        result1=[result[i] for i in range (1,len(result)) if result[i][6]==diff ]
        
        if len(result1)<number//2:
            raise ValueError("we cannot form the quiz")
        for i in range (0,number//2):        
            rdm=randint(0,len(result1)-1)
            final=result1[rdm]
            list.append(final)
            del result1[rdm]
        for i in range(number//2,number):
            rdm=randint(0,len(result))
            final=result[rdm]
            list.append(final)
        print(list)
        '''
        this function calls write to file
        in order to store in the given file
        the list we obtained (thr quiz)
        '''
        self.writeToFile(filename,list)
            
    def writeToFile(self,filename,list):
        '''
        input-list reveived
        outpu-write to the filename file list 
        corresponding question
        '''
        f=open(filename,'w')
        try:
            for  i in list:
                
                for j in i:
                    f.write(str(j))
                    f.write(';')
                f.write('\n')
            f.close()    
        except Exception as e:
            print(e)
            
            
    def start(self,filename):
        '''
        this function read a file already
        written and read it line by line
        after it order the questions by difficulty
        it will store in list the results in asscendong 
        oreder of difficulty
        and return the result
        '''
        l=[]
        result=[]
        try:   
            f=open(filename,'r')
            line=f.readline().strip()
            while len(line)>0:
                line=line.split(';')
                result.append([line[0],line[1],line[2],line[3],line[4],line[5],line[6]])
                line=f.readline().strip()
            f.close()
        except IOError as e:
            print(e)
        return result

        for i in result:
            if result[i][6]=='easy':
                l.append(result[i]) 
        for i in result:
            if result[i][6]=='medium':
                l.append(result[i]) 
        for i in result:
            if result[i][6]=='hard':
                l.append(result[i]) 
        return result










        
