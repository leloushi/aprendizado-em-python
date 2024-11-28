import socket
import sys


ip = sys.argv[1]
porta = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, porta))

msg = s.recv(1024).decode()
senha = input(msg)
s.send(senha.encode())

while True:
	print(s.recv(1024).decode())

	msg = input("> ")
	msg += "\n"

	s.send(msg.encode())
