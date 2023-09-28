import os
import csv
from Login.register_debug import cvsMaker
debugMode: bool = True
# data_path: str = os.path.abspath("Login")
# cvs_path = os.path.join(data_path, 'logs.csv')
data_path: str = os.path.abspath("logs.csv")


def login(user: str, password: str) -> (bool, str):
    userMatch: bool = False
    passMatch: bool = False
    try:
        with open(data_path, mode='r+') as data:
            reader = csv.reader(data)
            next(reader)
            print(reader)
            for row in reader:
                if row[1] == user:
                    userMatch = True
                    if row[2] == password:
                        passMatch = True
                        # row[2] = 'True'
                        # Llamar a funcion de session_state
    except FileNotFoundError as error:
        cvsMaker()
        if debugMode:
            print(error)
    if userMatch:
        print(f'user already exists: {user}')
    elif userMatch == False:
        print(f'non-existent user: {user}')

    if passMatch:
        print(f'Access with password: {password}')
        return True
    elif passMatch == False:
        print(f'wrong password {password}')
