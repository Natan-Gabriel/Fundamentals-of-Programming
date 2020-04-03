from random import randint
class Repo:
    def __init__(self,a,b,c,d,e,f,g,h):
        self.__starve=a
        self.__came=b
        self.__population=c
        self.__owns=d
        self.__harvest=e
        self.__rats=f
        self.__price=g
        self.__stocks=h
    def getOwns(self):
        return self.__owns
    def getHarvest(self):
        return self.__harvest
    def getPopulation(self):
        return self.__population
    def getStocks(self):
        return self.__stocks
    def starve(self,y):
        '''
        this function computes the numebr of persons who starved
        '''
        self.__starve=0
        if self.__population-y//20>0:
            self.__starve=self.__population-y//20
        if self.__population<=self.__starve*2:
            self.__starve=-1 
            return  
            
        return self.__starve

    def came(self):
        '''
        this function computes is a number random 
        of persons , between 0 and 10 came to the city ,
        in case which no people starved
        '''
        
        x=0
        if self.__starve==0:
            x=randint(0,10)
            self.__population+=x
        return x
    def owns(self,x):
        
        '''
        this computes the numbers of acres
        owned by Hammurabbi
        '''
        return self.__owns+x
    def harvest(self,x):
        '''
        this function generates a random integer which 
        will represents how many units people can harvest
        on an acre
        '''
        
        y=randint(1,6)
        self.__harvest=y
        return y
    def rats(self):
        '''
        this function computes the number of unites
        which was eaten by rats,if any
        '''
        z=0
        y=randint(1,5)
        if y==1:
            max=1/10*self.__stocks
            z=randint(0,int(max))
            self.__stocks-=z
        return z
            
        
    def price(self,z):
        '''
        this function computes the price,random 
        between 15 and 25 of an acre,in units
        and return it
        '''
        price=randint(15,25)
        self.__price=price
        return price
    def stocks(self,x,y):
        '''
        this function computes the number of 
        stocks of grain owned by 
        Hammurrabi
        '''
        self.__stocks-=x*self.__price
        self.__stocks-=y
        z=randint(1,10)
        self.__stocks+=self.__population*8*self.__harvest
        return self.__stocks
    def population(self):
        
        '''
        this function return the population
        '''
        return self.__population
    def end(self):
        '''
        this function returns 0 if you lost 
        and 1 if you won
        '''
        a=0
        if self.__population>100 and self.__owns>1000:
            a=1
        return a
    def died(self):
        '''
        this function end the game if more that a half 
        of population starved and returns True
        '''
        if self.__starve<0:
            return True
        

    
    
        