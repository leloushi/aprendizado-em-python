import socket
import sys

port = int(sys.argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("0.0.0.0", port))

print(f"Aguardando conexão UDP 0.0.0.0 {port}")

while True:
	dados, client = s.recvfrom(1024)
	print(f"{client} - {dados.decode()}")

	msg = input("> ")
	s.sendto(msg.encode(),client)
