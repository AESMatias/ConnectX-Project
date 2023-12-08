import os
import sys
import requests
import json
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)


def register(user: str, password: str) -> bool:
    url = 'http://localhost:8000/Register'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload = {
        'username': user,
        'password': password
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return True
    return False

# from Login.bd import TABLEUSERS, connect_to_db
# import os
# import sys
# project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(project_root)


# def tableMaker() -> None:
#     db = connect_to_db()
#     mycursor = db.cursor()
#     mycursor.execute(TABLEUSERS)
#     mycursor.close()
#     db.close()


# def register(user: str, password: str) -> bool:
#     tableMaker()
#     db = connect_to_db()
#     mycursor = db.cursor()
#     mycursor.execute("SELECT nickName FROM Users")
#     result = mycursor.fetchall()
#     user_exists = False
#     for row in result:
#         if user == row[0]:
#             user_exists = True
#             print('User already exists, choose another user')
#             return False
#     if not user_exists:
#         mycursor.execute(
#             "INSERT INTO Users (nickName, password, sessionState) VALUES (%s,%s,%s)", (user, password, 0))
#         db.commit()
#     mycursor.close()
#     db.close()
#     return True
