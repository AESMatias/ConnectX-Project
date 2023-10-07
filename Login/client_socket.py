from PyQt6.QtCore import QTimer, QCoreApplication, Qt, QObject, pyqtSignal, QThread, QRunnable, QThreadPool, QEventLoop, QEvent
import socket
from typing import Optional, List, Dict, Set, Tuple, Union, Any, Literal, Text
from PyQt6.QtGui import QPixmap, QCursor


class ClientCommunicator(QObject):
    message_received = pyqtSignal(str)

    def __init__(self, host, port, username):
        super().__init__()
        self.host = host
        self.port = port
        self.client_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self.username = username

    def run_client(self):
        print('run_client')
        try:
            self.client_socket.connect((self.host, self.port))
            print(self.username)
            while True:
                message = input('Write a message:\n')
                if message.lower() == 'exit' or message.lower() == 'close':
                    self.client_socket.sendall(message.encode())
                    response = self.client_socket.recv(4096)
                    response = response.decode('utf-8')

                    self.message_received.emit(f"{self.username}: {response}")

                    self.client_socket.send(message.encode())
                    self.client_socket.close()
                    break

                # Sending message to the server
                self.client_socket.send(message.encode())
                print('Message sent')

                # Receiving message from the server
                response = self.client_socket.recv(4096)
                response = response.decode('utf-8')
                self.message_received.emit(f"{self.username}: {response}")

        except ConnectionError as e:
            print('Connection error', e)
        finally:
            print('finallyyy')
            self.client_socket.close()
