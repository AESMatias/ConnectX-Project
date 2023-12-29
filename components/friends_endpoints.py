import requests


def reject_friend_request(token: str, to_username: str) -> None:
    to_username = to_username.strip()
    to_username = str(to_username)
    url = 'http://localhost:8000/friend/request/reject'

    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {str(token)}'
    }
    params = {
        'username': str(to_username)
    }

    try:
        response = requests.put(url, headers=headers, params=params)
        if response.status_code == 200:
            pass
            # TODO: put a qlabel message that indicates that the message was sent or not
        else:
            print(
                f"Error rejecting the friend request. Status code: {response.status_code}")
            print(response.text)
    except requests.RequestException as e:
        print(f"Connection error: {e}")


def accept_friend_request(token: str, to_username: str) -> None:
    to_username = to_username.strip()
    to_username = str(to_username)
    url = 'http://localhost:8000/friend/request/accept'

    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {str(token)}'
    }
    params = {
        'username': str(to_username)
    }

    try:
        response = requests.put(url, headers=headers, params=params)
        if response.status_code == 200:
            pass
            # TODO: put a qlabel message that indicates that the message was sent or not
        else:
            print(
                f"Error accepting the friend request. Status code: {response.status_code}")
            print(response.text)
    except requests.RequestException as e:
        print(f"Connection error: {e}")


def send_request(self, token: str, to_username: str) -> None:
    to_username = to_username.strip()
    to_username = str(to_username)
    url = 'http://localhost:8000/friend/request'

    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {str(token)}'
    }
    params = {
        'username': str(to_username)
    }

    try:
        response = requests.post(url, headers=headers, params=params)
        if response.status_code == 200:
            pass
            # TODO: put a qlabel message that indicates that the message was sent or not
        else:
            print(
                f"Error sending the friend request. Status code: {response.status_code}")
            print(response.text)
    except requests.RequestException as e:
        print(f"Connection error: {e}")


def get_pendient_friends(self, token: str) -> list:
    # token = str(token)
    url = 'http://localhost:8000/friends/pendient'
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {str(token)}'
    }
    # params = {
    #     'username': str(to_username)
    # }

    try:
        response = requests.get(url, headers=headers)
        # sacamos la data de response
        data = response.json()
        if response.status_code == 200:
            return list(data)
        else:
            print(
                f"Error getting the list of pendient friends. Status code: {response.status_code}")
            print(response.text)
    except requests.RequestException as e:
        print(f"Connection error: {e}")


def get_friend_list(self, token: str) -> list:
    url = 'http://localhost:8000/friends'
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {str(token)}'
    }
    # params = {
    #     'username': str(to_username)
    # }

    try:
        response = requests.get(url, headers=headers)
        # sacamos la data de response
        data = response.json()
        if response.status_code == 200:
            return list(data)
        else:
            print(
                f"Error getting the list of friends. Status code: {response.status_code}")
            print(response.text)
    except requests.RequestException as e:
        print(f"Connection error: {e}")
