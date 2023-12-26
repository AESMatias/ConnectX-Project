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
        print('EL TOKEN INICIAL ES ', access_token)
        return True, access_token
    return False, response.text
