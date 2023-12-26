import requests


def reject_friend_request(token: str, to_username: str) -> None:
    to_username = to_username.strip()

    # token = str(token)
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
            print(f"SOLICITUD RECHAZADA a {to_username} CON [EXITO]")
            # TODO put a qlabel message that indicates that the message was sent or not
        else:
            print(
                f"Error al enviar el mensaje. Código de estado: {response.status_code}")
            print(response.text)
    except requests.RequestException as e:
        print(f"Error de conexión: {e}")


def accept_friend_request(token: str, to_username: str) -> None:
    to_username = to_username.strip()

    # token = str(token)
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
            print(f"SOLICITUD ACEPTADA a {to_username} CON [EXITO]")
            # TODO put a qlabel message that indicates that the message was sent or not
        else:
            print(
                f"Error al enviar el mensaje. Código de estado: {response.status_code}")
            print(response.text)
    except requests.RequestException as e:
        print(f"Error de conexión: {e}")


def send_request(self, token: str, to_username: str) -> None:
    to_username = to_username.strip()

    # token = str(token)
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
        print('EL TOKEN FINAAAL ES ', token)
        if response.status_code == 200:
            print(f"SOLICITUD enviada a {to_username} con [EXITO]")
            # TODO put a qlabel message that indicates that the message was sent or not
        else:
            print(
                f"Error al enviar el mensaje. Código de estado: {response.status_code}")
            print(response.text)
    except requests.RequestException as e:
        print(f"Error de conexión: {e}")


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
            print(f"Amigos pendientes: {data}")
            return list(data)
        else:
            print(
                f"Error al enviar el mensaje. Código de estado: {response.status_code}")
            print(response.text)
    except requests.RequestException as e:
        print(f"Error de conexión: {e}")


def get_friend_list(self, token: str) -> list:

    # token = str(token)
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
            print(f"lista de amigos: {data}")
            return list(data)
        else:
            print(
                f"Error al enviar el mensaje. Código de estado: {response.status_code}")
            print(response.text)
    except requests.RequestException as e:
        print(f"Error de conexión: {e}")
