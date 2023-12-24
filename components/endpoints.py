import requests
import json
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout
import time
from typing import Tuple
import aiohttp


def active_users(self) -> Tuple[bool, str]:
    print('active_users function in chat.py every 15 seconds')
    url = 'http://localhost:8000/active/'
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        active_users_decoded = response.content.decode('utf-8')
        list_of_active_users = json.loads(active_users_decoded)
        self.active_users_chat = len(
            list_of_active_users), list_of_active_users
        self.labels['username'].setText(
            f'{self.active_users_chat[0]} Users online')
        self.labels['users_active'].setText('Active users: \n \n{}'.format(
            '\n'.join(self.active_users_chat[1])))
        return len(list_of_active_users), list_of_active_users

    elif response.status_code == 404:
        print('status_code 404 active users')


def last_n_messages(self, n: str) -> list[str]:
    print(f'Charging last {n} messages')
    url = 'http://localhost:8000/messages/'
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers)

    messages_to_return: list = []

    if response.status_code == 200:
        data_decoded = response.content.decode('utf-8')
        data_loaded = json.loads(data_decoded)

        for message in data_loaded:

            message_time = message['datatime'][11:16]
            formatted_message = f"{message_time} - {message['username']}: {message['mensaje']}"
            messages_to_return.append(formatted_message)
        messages_to_return
        return messages_to_return[0:n]

    elif response.status_code == 404:
        print('status_code 404 active users')
        return ['No messages found: 404']
