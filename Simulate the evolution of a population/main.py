from validator import Validator
from console import Console
from service import Service
from repo import Repo

repo=Repo(0,0,100,1000,3,200,20,2800)
validator=Validator(repo)
service=Service(repo,validator)
console=Console(service)
console.main()