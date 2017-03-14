import abc
import appdirs
import argparse
import http
import ipaddress
import logging
import sys
import socket
import uuid

from multiprocessing.pool import Pool

class Server:
    @staticmethod
    def connect(host='127.0.0.1', port=4200):
        listen_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_soc.bind((host, port))
        listen_soc.listen(1)

        print('Semiconductor running on {}:{}'.format(host, port))

        while True:
            client_connection, client_address = listen_soc.accept()
            request = client_connection.recv(1024)

            print(request)

            http_response = b"Hello"

            client_connection.sendall(http_response)
            client_connection.close()


if __name__ == '__main__':
    s = Server
    s.connect()
