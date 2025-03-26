import socket

class Client: # Class that handles the socket
    def __init__(self, url): # Constructor
        self.url = url
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # The client, sends request to server

    def send(self, message): # Sends a message to the client
        self.client_socket.send(message)

    def recv(self, amount): # Receives certain amount of bytes
        return self.client_socket.recv(amount)

    def connect(self): # start the client
        self.client_socket.connect((self.url, 80))

    def close(self): # Closes the client
        self.client_socket.close()