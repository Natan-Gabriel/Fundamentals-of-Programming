class Sort1:
    def __init__(self,arr,max=0):
        self.__arr=arr
        self.max = max

    def __setItem__(self,key,value):
        self.__value[key]=value
    def __delItem__(self,key):
        del self.__arr[key]


    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            #result = 2 ** self.n
            self.n += 1
            return self.array[self.n]
        else:
            raise StopIteration  

        
        
    def gnomeSort(self,greater): 
        index = 1
        while index < len(self.__arr): 
            if index == 0: 
                index = index + 1
            if greater(self.__arr[index],self.__arr[index - 1])==True: 
                index = index + 1
            else: 
                self.__arr[index], self.__arr[index-1] = self.__arr[index-1], self.__arr[index] 
                index = index - 1
      
        return self.__arr


    def filter1(self,acceptance):
        data=[]
        for i in self.__arr:
            if acceptance(i):
                data.append(i)
        return data

def greater1(a,b):
    if a>=b:
        return True
    else:
        return False
def acceptance(x):
    if x>10:
        return True       
