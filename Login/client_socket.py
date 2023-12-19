from PyQt6.QtCore import QTimer, QCoreApplication, Qt, QObject, pyqtSignal, QThread, QRunnable, QThreadPool, QEventLoop, QEvent
import socket
from typing import Optional, List, Dict, Set, Tuple, Union, Any, Literal, Text
from PyQt6.QtGui import QPixmap, QCursor
from threading import Thread
from PyQt6.QtNetwork import QTcpSocket

# TODO: Here, we need to change the way we are sending the username to the server


class ClientCommunicator(QObject):
    message_received = pyqtSignal(str)
    client_ready = pyqtSignal()

    def __init__(self, host, port, username):
        super().__init__()
        self.host = host
        self.port = port
        self.username = username
        self.client_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self.send_message_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self._stop_threads = False  # Bandera para detener los hilos
        self.socket_connected()
        self.first_message = True

    def socket_connected(self):
        self.client_ready.emit()

    def send_message(self, message: str) -> None:
        if self.is_running():
            try:
                if message.lower() == 'exit' or message.lower() == 'close':
                    print('Sending closing request to the server')
                    # message = f"{self.username}: {message}"
                    message = str(message)

                    self.send_message_socket.send(message.encode('utf-8'))
                    # self.client_socket.close()
                    # self.send_message_socket.close()
                    self.message_received.emit('connecton_closed')
                # message = f"{self.username}: {message}"
                self.send_message_socket.send(message.encode('utf-8'))
            except OSError as e:
                print(f"Error sending message: {e} AAAAAAAAAAAAAAA")

    def is_running(self):
        # Verifica si el socket está conectado
        return self.send_message_socket and self.send_message_socket.fileno() != -1

    def receive_messages(self) -> None:
        try:
            while True:
                data = self.client_socket.recv(4096)
                if not data:
                    print('Connection closed without data')
                    self.client_socket.close()
                    self.send_message_socket.close()
                    break
                elif data.decode('utf-8').endswith('close_the_connection'):
                    print('Connection closed from the server')
                    self.client_socket.close()
                    self.send_message_socket.close()
                    break
                elif data:
                    data = data.decode('utf-8')
                    username, message = data.split(':')
                    print(f"Received: {message} from {username}")
                    if message.__contains__('MESSAGE_LOGIN'):
                        continue
                    else:
                        # Send the signal to the main thread
                        self.message_received.emit(data)
        except Exception as e:
            print("Error receiving message:", str(e))
            # self.client_socket.close()
            # self.send_message_socket.close()

    def run_client(self) -> None:
        try:
            print('NEW THREADDD iniciado con run_client',
                  self.username, self.host, self.port)

            self.client_socket.connect((self.host, self.port))
            self.send_message_socket.connect((self.host, self.port))

            # This thread receives messages from the server
            # TODO: we need to use QThread instead of Thread
            receive_thread = Thread(target=self.receive_messages, daemon=True)
            receive_thread.start()

        except ConnectionError as e:
            print('Connection error at run_client inside ClientCommunicator:', e)
            self.client_socket.close()
            self.send_message_socket.close()


class ClientThread(QThread):
    def __init__(self, communicator):
        super().__init__()
        self.communicator = communicator

    def run(self):
        self.communicator.run_client()
