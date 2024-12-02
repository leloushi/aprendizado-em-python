import socket
import sys

ip = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor = (ip, port)

while True:
	msg = input ("> ")
	s.sendto(msg.encode(), servidor)

	dados, sys = s.recvfrom(1024)
	print(f"{sys} - {dados.decode()}")
