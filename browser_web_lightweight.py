import socket
import client
from urllib.parse import urlparse
import os

class Website:
    def __init__(self): # Creates the
        self.client = client.Client()
        self.url = "http://www.testingmcafeesites.com/" # input("Please enter the URL of the website you to access: \n")
        self.fixed_url = urlparse(self.url).netloc
        self.path = urlparse(self.url).path
        self.sources = []
        self.access_server()


    def access_server(self): # Gets The URL and addresses the server
        ip = socket.gethostbyname(self.fixed_url)
        self.client.connect(ip)

        self.send_request("GET") # initial request
        self.handle_response()

    def send_request(self, req_type):
        request = f"{req_type} {self.path} HTTP/1.1\r\nHost:{self.fixed_url}\r\n\r\n"
        self.client.send(request.encode())

        if req_type == "POST":
            request += "Content-Type: application/x-www-form-urlencoded\r\n\r\n"

    def handle_response(self):
        data = self.client.recv(8000)
        decoded_data = data.decode()
        print(decoded_data)
        status_code = int(decoded_data.split('\r\n')[0].split(' ')[1])
        if status_code == 200 and not os.path.isdir("." + self.fixed_url):
            os.mkdir("www." + self.fixed_url)

w1 = Website()
