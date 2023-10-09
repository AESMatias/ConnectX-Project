from Login.bd import connect_to_db, checkTable
import os
import sys
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
db = connect_to_db()
mycursor = db.cursor()


def update_session_state(user: str, new_state: bool) -> None:
    db = connect_to_db()
    mycursor = db.cursor()
    new_state = int(new_state)
    update_query = "UPDATE Users SET sessionState = %s WHERE nickName = %s"
    mycursor.execute(update_query, (new_state, user))
    db.commit()
    mycursor.close()
    db.close()


def changeName(user: str, newUsername: str) -> str:
    db = connect_to_db()
    mycursor = db.cursor()
    mycursor.execute(
        "UPDATE Users SET nickName = %s WHERE nickName = %s", (newUsername, user))
    db.commit()
    mycursor.close()
    db.close()


def changePassword(user: str, newPassword: str) -> str:
    db = connect_to_db()
    mycursor = db.cursor()
    mycursor.execute(
        "UPDATE Users SET password = %s WHERE nickName = %s", (newPassword, user))
    db.commit()
    mycursor.close()
    db.close()
