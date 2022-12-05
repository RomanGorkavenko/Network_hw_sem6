import socket
import threading
from time import sleep

ip = "127.0.0.1"
port = 50222

sock = socket.socket()
addr = (ip, port)
sock.connect(addr)

data_out = input()
sock.send(data_out.encode('ascii'))


def recieving():
    while True:
        data_chunk = sock.recv(1024)
        if data_chunk:
            print(data_chunk)


def write():
    msg = input()
    sock.send(msg.encode('ascii'))
    return msg


rec_thread = threading.Thread(target=recieving)
rec_thread.start()

while True:
    if write() == "exit":
        break
# write_thread = threading.Thread(target=write)
# write_thread.start()

sock.close()
