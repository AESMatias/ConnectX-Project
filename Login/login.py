import os
import sys
import requests
from typing import Tuple

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# login ahora retorna el jwt del usuario


def login(user: str, password: str) -> Tuple[bool, str]:
    global access_token
    url = 'http://localhost:8000/token'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {
        'username': user,
        'password': password
    }
    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        access_token = response.json()["access_token"]
        return True, access_token
    return False, response.text


# def logout(user: str) -> bool:
#     update_session_state(user, False)
#     return False, "Logout successful"

# from Login.bd import connect_to_db
# import os
# import sys
# from typing import Tuple
# project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(project_root)


# def login(user: str, password: str) -> Tuple[bool, str]:
#     db = connect_to_db()
#     mycursor = db.cursor()
#     mycursor.execute("SELECT password FROM Users WHERE nickName = %s", (user,))
#     result = mycursor.fetchone()
#     if result is None:
#         return False, "User does not exist"
#     elif result[0] != password:
#         return False, "Incorrect password"
#     else:
#         """
#         mycursor.execute("UPDATE Users SET sessionState = false") #Change all existing sessions, Cambiar cuando sean mas de 2 usuarios en sesion
#         db.commit() """
#         update_session_state(user, True)
#         db.commit()
#         mycursor.close()
#         db.close()
#         return True, "Successful login"


# def logout(user: str) -> bool:
#     update_session_state(user, False)
#     return False, "Logout successful"
