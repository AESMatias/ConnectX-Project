import os,csv 
from register_module import cvsMaker
debugMode: bool = True
data_path: str = os.path.abspath("logs.csv")

def login(user:str, password:str) -> None:
    userMatch: bool = False
    passMatch: bool = False
    try:
        with open(data_path, mode='r+') as data:
            reader = csv.reader(data)
            next(reader)
            for row in reader:
                if row[0] == user:
                    userMatch = True
                    if row[1] == password:
                        passMatch = True  
                        row[2] == 'True'
    except FileNotFoundError as error:
        cvsMaker()
        if debugMode:
            print(error)
    if userMatch:
        print('user already exists')
    elif userMatch == False:
        print('non-existent user')
    if passMatch:
        print('Aceso')
        
    elif passMatch == False:
        print('wrong password')
    
login('Exdi','pepe')