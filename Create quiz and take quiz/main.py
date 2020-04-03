from ui import Ui
from controller import Controller
from repo import Repo

repo=Repo()
controller=Controller(repo)
c=Ui(controller)
c.run()