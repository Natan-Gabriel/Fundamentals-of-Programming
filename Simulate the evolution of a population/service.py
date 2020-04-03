
class Service:
    def __init__(self,repo,validator):
        self.__repo=repo
        self.__validator=validator
    def starve(self,y):
        return self.__repo.starve(y)
    def came(self):
        return self.__repo.came()
    def owns(self,x):
        return self.__repo.owns(x)
    def harvest(self,x):
        self.__validator.buy(x)
        return self.__repo.harvest(x)
    def rats(self):
        return self.__repo.rats()
    def price(self,z):
        return self.__repo.price(z)
    def stocks(self,x,y):
        return self.__repo.stocks(x,y)
    def population(self):
        return self.__repo.population()
    def end(self):
        return self.__repo.end()
    def died(self):
        return self.__repo.died()