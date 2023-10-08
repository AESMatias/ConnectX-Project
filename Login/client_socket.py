from PyQt6.QtCore import QTimer, QCoreApplication, Qt, QObject, pyqtSignal, QThread, QRunnable, QThreadPool, QEventLoop, QEvent
import socket
from typing import Optional, List, Dict, Set, Tuple, Union, Any, Literal, Text
from PyQt6.QtGui import QPixmap, QCursor
from threading import Thread


class ClientCommunicator(QObject):
    message_received = pyqtSignal(str)

    def __init__(self, host, port, username):
        super().__init__()
        self.host = host
        self.port = port
        self.client_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self.username = username
        self.send_message_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

    def send_message(self, message):
        if message.lower() == 'exit' or message.lower() == 'close':
            self.send_message_socket.sendall(message.encode('utf-8'))
            response = self.send_message_socket.recv(4096)
            response = response.decode('utf-8')
            self.message_received.emit(f"{self.username}: {response}")
            self.send_message_socket.send(message.encode())

        # Sending message to the server
        message = f"{self.username}: {message}"
        self.send_message_socket.send(message.encode('utf-8'))
        # self.message_received.emit(f"response")

    def receive_messages(self):
        print('receive_messages funcitiooon')
        try:
            while True:
                data = self.client_socket.recv(4096)
                if not data:
                    print('Connection closed')
                    break
                elif data == 'closed':
                    print('Connection closed from the successfully')
                    self.client_socket.close()
                    break
                elif data:
                    data = data.decode('utf-8')
                    print(f"Received: {data}")
                    # Emitir la señal en el hilo principal
                    self.message_received.emit(data)
        except Exception as e:
            print("Error receiving message:", str(e))

    def run_client(self):
        print('run_client, chat socket has been started!')
        try:
            # self.client_socket = socket.socket(
            #     socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
            self.send_message_socket.connect((self.host, self.port))

            # TODO: This thread receives messages from the server
            receive_thread = Thread(target=self.receive_messages)
            receive_thread.start()

            # receive_thread = QThread()
            # receive_thread.started.connect(self.receive_messages)
            # receive_thread.start()

            # while True:
            #     message = input('Write a message:\n')
            #     if message.lower() == 'exit' or message.lower() == 'close':
            #         self.client_socket.sendall(message.encode())
            #         response = self.client_socket.recv(4096)
            #         response = response.decode('utf-8')

            #         self.message_received.emit(f"{self.username}: {response}")

            #         self.client_socket.send(message.encode())
            #         self.client_socket.close()
            #         break

            # # Sending message to the server
            # message = f"{self.username}: {message}"
            # self.client_socket.send(message.encode())

            # # Receiving message from the server
            # response = self.client_socket.recv(4096)
            # response = response.decode('utf-8')
            # self.message_received.emit(f"response")

        except ConnectionError as e:
            print('Connection error', e)
            self.client_socket.close()
            self.send_message_socket.close()
        finally:
            print('finallyyy')
            # self.client_socket.close()


class ClientThread(QThread):
    def __init__(self, communicator):
        super().__init__()
        self.communicator = communicator

    def run(self):
        self.communicator.run_client()
