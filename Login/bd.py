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
# Configuración de la conexión a la base de datos
def connect_to_db() -> None:
    return mysql.connector.connect(
        user = 'root',
        password = 'o3Sq4FNPIrI0xYoYgQQM',
        host = 'containers-us-west-75.railway.app',
        database = 'railway',
        port = 6336
    )


def checkTable() -> str:
    db = connect_to_db()
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM Users")
    for x in mycursor:
        print(x)

def drop_table(Tabla:str) -> None:
    db = connect_to_db()
    mycursor = db.cursor()
    mycursor.execute(f"DROP TABLE IF EXISTS {Tabla}")
    mycursor.close()
    db.close()      
    mycursor.close()
    db.close()    