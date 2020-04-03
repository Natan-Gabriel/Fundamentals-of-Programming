class Console:
    def __init__(self,service):
        self.__service=service
    def __starve(self,y):
        return self.__service.starve(y)
    def __came(self):
        return self.__service.came()
    def __owns(self,x):
        return self.__service.owns(x)
    def __harvest(self,x):
        return self.__service.harvest(x)
    def __rats(self):
        return self.__service.rats()
    def __price(self,z):
        return self.__service.price(z)
    def __stocks(self,x,y):
        return self.__service.stocks(x,y)
    def __population(self):
        return self.__service.population()
    def __end(self):
        return self.__service.end()
    def __died(self):
        return self.__service.died()
    def __buy(self,x):
        pass
        #self.__validator.buy(x)
    def __feed(self,y):
        pass
        #self.__validator.feed(y)
    def __plant(self,z):
        pass
        #self.__validator.plant(z)
    
    
    def main(self):
        year=0
        status=True
        while status==True:
            try:
                
                x=int(input("Acres to buy/sell(+/-)-> " ))
                self.__buy(x)
                y=int(input("Units to feed the population-> " ))
                self.__feed(y)
                z=int(input("Acres to plant-> " ))
                self.__plant(z)
                
                
                h=self.__harvest(x)
                pr=self.__price(z)
                
                s=self.__starve(y)
                if self.__died==True:
                    print('Game over')
                    return
                st=self.__stocks(x,y)
                c=self.__came()
                o=self.__owns(x)
                
                r=self.__rats()
                
                
                p=self.__population()
                print('In year',str(year)+','+str(s),'people starved')
                print(str(c),'people came to the city')
                print('City population is',p)
                print('City owns',o,'acres of land')
                print('Harvest was',h,'units per acre')
                print('Rats ate',r,'units')
                print('Land price is',pr,'units per acre')
                print('Grain stocks are',st,'units')
                print('\n')
                year+=1
            except ValueError as e:
                print(e)
            if year==6:
                status=False

        if self.__end==0:
            print('You did not do well')
        else:
            print("Congrats")




