import socket
import client

while True:
    url = input("Please enter the URL of the website you to access: \n")
    server = client.Client(url)

    server.connect()
    request = f"GET /{url} HTTP/1.0\r\n Host:"