import os
import csv
import uuid

debugMode: bool = False
data_path: str = os.path.abspath("logs.csv")


cvs_colums = ['id', "users", 'password', 'session_state', 'userPath' , "imgPath"]

def cvsMaker() -> None:
    with open(data_path, mode='w', newline="") as data:
        writer = csv.writer(data)
        writer.writerow(cvs_colums)
        print('> New CVS created')

def id () -> (str):
    random_uuid = uuid.uuid4()
    limited_random_id = str(random_uuid)[:6]
    return str(limited_random_id)

def userPath(user: str, id: str) -> str:
    base_directory = os.path.dirname(os.path.abspath(__file__))
    users_directory = os.path.join(base_directory, "Users")
    user_directory = os.path.join(users_directory, f"{user}_{id}")
    
    if not os.path.exists(user_directory):
        os.makedirs(user_directory)
    
    return user_directory





'''def userPath(user: str,id: str) -> str:
   base_directory = os.path.dirname(os.path.abspath(__file__))
   username = user
   user_directory = os.path.join(base_directory, "Users", f"{username}_{id}")
   if not os.path.exists(user_directory):
    os.makedirs(user_directory)
    return f"{user_directory}"    '''




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
        userId = id()
        Pathdirectory = userPath(user, userId)
        pathImguser = f"{user}-{userId}_img.jpg"
        newUser = [userId, user, password, False, Pathdirectory, pathImguser]
        with open(data_path, mode='a', newline='') as data:
            writer = csv.writer(data)
            writer.writerow(newUser)
            if debugMode:
                print('Usuario Creado')

Register('Enrique','UnoDosTres')

""" 
Add
    User_path
    fecha de Creacio
    hacer que el usuario sea un id no un nombre
"""