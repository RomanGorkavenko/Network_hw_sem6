import socket
from threading import Thread

HOST = '127.0.0.1'
PORT = 55555
ADDR = (HOST, PORT)
BUF = 1024
clients = set()
separator = "<SEP>"

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)

server.listen()
print(f"Прослушивание {HOST}:{PORT}")


def listen_client(cs):
    global msg
    while True:
        try:
            msg = cs.recv(BUF).decode()
        except Exception as e:
            print(f"Ошибка: {e}")
            clients.remove(cs)
        else:
            msg = msg.replace(separator, ": ")
        for client in clients:
            client.send(msg.encode())


while True:
    client, client_address = server.accept()
    print(f"{client_address} присоединился.")
    clients.add(client)
    thread = Thread(target=listen_client, args=(client,))
    thread.daemon = True
    thread.start()

for cs in client_sockets:
    cs.close()
s.close()
