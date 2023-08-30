import os
import csv
debugMode: bool = True
data_path: str = os.path.abspath("logs.csv")


def cvsMaker() -> None:
    with open(data_path, mode='w', newline="") as data:
        writer = csv.writer(data)
        writer.writerow(["users", 'password', 'session_state'])
        print('> New CVS created')


def Register(user: str, password: str) -> None:
    userExist: bool = False
    try:  # Check if user exists
        with open(data_path, mode='r') as data:
            reader = csv.reader(data)
            next(reader)
            for row in reader:
                if row[0] == user:
                    userExist = True
                    print('duplicate User')
                    break
    except FileNotFoundError as filenotfound:
        try:
            cvsMaker()
            if debugMode:
                print(filenotfound)
        except Exception as error:
            print(error)
    if not userExist:  # add
        newUser = [user, password, False]
        with open(data_path, mode='a', newline='') as data:
            writer = csv.writer(data)
            writer.writerow(newUser)
            if debugMode:
                print('Usuario Creado')


""" Register('jose','pepe')
Register('juan','equisde')
Register('Numero','pepe')
Register('nichol','dsadsada')
Register('brenwod','dsaaF')
Register('jodsadse','pepe')
Register('Exdi','pepe')  """
