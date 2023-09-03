from bd import TABLEUSERS,connect_to_db

def tableMaker() -> None:
    db = connect_to_db()
    mycursor = db.cursor()
    mycursor.execute(TABLEUSERS)
    mycursor.close()
    db.close()

def register(user:str, password: str) -> None:
    tableMaker()
    db = connect_to_db()
    mycursor = db.cursor()
     #Create Table
    #Check if user exist in table
    mycursor.execute("SELECT nickName FROM Users")
    result = mycursor.fetchall()
    user_exists = False
    for row in result:
        if user == row[0]:
            user_exists = True
            print('User already exists, choose another user')
            break
    if not user_exists:
        mycursor.execute("INSERT INTO Users (nickName, password, sessionState) VALUES (%s,%s,%s)",(user,password,0))
        db.commit()
    mycursor.close()
    db.close()
