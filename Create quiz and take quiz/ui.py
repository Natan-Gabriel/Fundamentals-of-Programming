class Ui:
    def __init__(self,controller):
        self.__controller=controller
    def __add(self,parts,a,filename):
        self.__controller.add(parts,a,filename)
    def __create(self,parts):
        self.__controller.create(parts)
    def __start(self,file):
        return self.__controller.start(file)
    
    def run(self):
        while True:
            parts=input("Enter an instruction:").strip()
            parts1=parts.split(' ')
            parts=parts.split(';')
            instr=parts[0].split(' ')
            
            try:
                if instr[0]=='add':
                    '''
                    example of command: add 12;Which number is not prime?;2;32;11;32;easy;
                    this fct will add a quiz with 3 options and a correct answer and with a given diff
                    '''
                    if not isinstance(parts[1],str) and not (parts[6]!='easy' and parts[6]!='medium' and parts[6]!='hard') and len(parts)!=7:
                        raise ValueError('Invalid input')
                    else:
                        self.__add(parts,instr[1],'master.txt')
                
                if parts1[0]=='create':
                    '''
                            input for self.__create:parts
                            self.__create creates a quiz 
                            on a given difficulty
                            with a given number of questions
                            and this quiz will be stored in 
                            a file specifed in parts
                            example: create easy 4 sample.txt
                    '''
                    if len(parts1)!=4 and not (parts1[1]!='easy' and parts1[1]!='medium' and parts1[1]!='hard'):
                        raise ValueError('Impossible file creation')
                    else:
                        self.__create(parts1)
                if parts1[0]=='start':
                    '''
                            use self.__start to take an already created test;
                            this function will also show you the result
                            for example: start sample.txt
                    '''
                    result=self.__start(parts1[1])
                    score=0
                    for i in range(0,len(result)):
                        print(result[i][1])
                        print(result[i][2],result[i][3],result[i][4])
                        x=input('Introduce an answer')
                        if x==result[i][5]:
                            if result[i][6]=='easy':
                                score+=1
                            if result[i][6]=='medium':
                                score+=2
                            if result[i][6]=='hard':
                                score+=3
                    print('Your score is '+str(score))
            except ValueError as e:
                print(e)