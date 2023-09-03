from bd import connect_to_db
db = connect_to_db()
mycursor = db.cursor()
pruebaUser = "Enrique"
pruebaPass = "root"
def update_session_state(user: str, new_state: bool) -> None:
    new_state = int(new_state)
    update_query = "UPDATE Users SET sessionState = %s WHERE nickName = %s"
    mycursor.execute(update_query, (new_state, user))
    db.commit()

update_session_state(pruebaUser, False)
mycursor.close()
db.close()
""" 
edit
    session_state [x]
    user,
    pass,
    img
"""
