from Login.edit import update_session_state
from Login.bd import connect_to_db
import os
import sys
from typing import Tuple
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)


def login(user: str, password: str) -> Tuple[bool, str]:
    db = connect_to_db()
    mycursor = db.cursor()
    mycursor.execute("SELECT password FROM Users WHERE nickName = %s", (user,))
    result = mycursor.fetchone()
    if result is None:
        return False, "User does not exist"
    elif result[0] != password:
        return False, "Incorrect password"
    else:
        """
        mycursor.execute("UPDATE Users SET sessionState = false") #Change all existing sessions, Cambiar cuando sean mas de 2 usuarios en sesion
        db.commit() """
        update_session_state(user, True)
        db.commit()
        mycursor.close()
        db.close()
        return True, "Successful login"


def logout(user: str) -> bool:
    update_session_state(user, False)
    return False, "Logout successful"
