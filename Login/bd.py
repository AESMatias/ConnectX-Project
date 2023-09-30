import mysql.connector

TABLEUSERS = """
    CREATE TABLE IF NOT EXISTS Users(
        userID INT AUTO_INCREMENT PRIMARY KEY, 
        nickName VARCHAR(50), 
        password VARCHAR(50), 
        sessionState BOOLEAN,
        creationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        
    )
"""

# Free to use for everyone lol


def connect_to_db() -> None:
    return mysql.connector.connect(
        user='root',
        password='o3Sq4FNPIrI0xYoYgQQM',
        host='containers-us-west-75.railway.app',
        database='railway',
        port=6336
    )


def checkTable() -> str:
    db = connect_to_db()
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM Users")
    for x in mycursor:
        print(x)
    mycursor.close()
    db.close()


def drop_table(Tabla: str) -> None:
    db = connect_to_db()
    mycursor = db.cursor()
    mycursor.execute(f"DROP TABLE IF EXISTS {Tabla}")
    mycursor.close()
    db.close()
