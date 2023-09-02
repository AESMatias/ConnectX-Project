import os
import pandas as pd
from register_module import cvsMaker
data_path: str = os.path.abspath("logs.csv")
df = pd.read_csv(data_path, on_bad_lines='warn') #'warn', raise a warning when a bad line is encountered and skip that line.


def save(index: int , column: str, new_value: str) -> None:
    df.loc[index, column] = new_value
    df.to_csv(data_path, index=False)  # Save edited CSV



def index(id: str,column: str):
    filtered_indices = df.loc[df[column] == id].index.tolist()



#def changeUser(id,new_Username)







""" 
edit
    session_state
    user,
    pass,
    img
"""

