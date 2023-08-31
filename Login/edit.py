import os
import csv
from register_module import cvsMaker
data_path: str = os.path.abspath("logs.csv")


def charge() -> None:
    memory = []

    with open(data_path, 'r+') as csvfile:
        reader = csvfile.read()
        memory.extend(eval(reader))
        print(memory)


'''def change(data):
     if data == memory: '''

charge()


# Estado actual de la sesion
# Nombre
# Password
