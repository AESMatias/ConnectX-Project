import os
import sys
import requests
from typing import Tuple
import asyncio
import aiohttp

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)


def login(user: str, password: str) -> Tuple[bool, str]:
    global access_token  # TODO: global variables are not recommended
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

    # async with aiohttp.ClientSession() as session:
    #     async with session.post(url, headers=headers, data=payload) as response:
    #         if response.status == 200:
    #             access_token = (await response.json())["access_token"]
    #             print('EL TOKEN INICIAL ES ', access_token)
    #             return True, access_token
    #         return False, await response.text()
