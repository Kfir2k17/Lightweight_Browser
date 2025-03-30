import socket
import client
from urllib.parse import urlparse
import os

class Website:
    def __init__(self): # Creates the
        self.client = client.Client()
        self.url = input("Please enter the URL of the website you to access: \n")
        self.fixed_url = urlparse(self.url).netloc
        self.path = urlparse(self.url).path
        self.sources = []


    def access_server(self): # Gets The URL and addresses the server
        ip = socket.gethostbyname(self.fixed_url)
        self.client.connect(ip)

        self.send_request("GET") # initial request
          data = self.client.recv(2048)



    def send_request(self, req_type):
        if req_type == "GET":
            request = f"GET {self.path} HTTP/1.1\r\nHost:www.{self.fixed_url}\r\n\r\n"
            self.client.send(request.encode())

    def read_file(self):
