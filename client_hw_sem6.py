import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init

init()

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED, Fore.YELLOW]

client_color = random.choice(colors)

HOST = '127.0.0.1'
PORT = 55555
ADDR = (HOST, PORT)
BUF = 1024
separator = "<SEP>"

s = socket.socket()
print(f"Подключение {HOST}:{PORT}...")
s.connect(ADDR)
print("Подключен.")
name = input("Введите Ваше имя: ")


def write_messages():
    while True:
        msg = s.recv(BUF).decode()
        print("\n" + msg)


t = Thread(target=write_messages)
t.daemon = True
t.start()
print("Введите сообщение:")

while True:
    to_send = input()
    if to_send.lower() == 'q':
        break
    date_now = datetime.now().strftime('%m-%d %H:%M')
    to_send = f"{client_color}[{date_now}] {name}{separator}{to_send}{Fore.RESET}"
    s.send(to_send.encode())

s.close()
