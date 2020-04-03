class Validator:
    def __init__(self,repo):
        self.__repo=repo
    def buy(self,x):
        own=self.__repo.getOwns()
        if -own>x:
            raise ValueError("Too much to sell")
        if x>self.__repo.getPopulation()*self.__repo.getHarvest()*10:
            raise ValueError('Too much to buy')
    def feed(self,y):
        if y>self.__repo.getStocks():
            raise ValueError("Too much to feed population")
    def plant(self,z):
        if self.__repo.getOwns()<z:
            raise ValueError("Too much to plant")
