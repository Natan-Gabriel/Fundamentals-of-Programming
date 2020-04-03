class Controller:
    def __init__(self,repo):
        self.__repo=repo
    def add(self,parts,a,filename):
        self.__repo.add(parts,a,filename)
    def create(self,parts):
        self.__repo.create(parts)
    def start(self,file):
        return self.__repo.start(file)