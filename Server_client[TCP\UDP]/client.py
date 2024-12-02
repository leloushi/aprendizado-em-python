import socket

class Client:

	def tcp(ip, port):

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))

		msg = s.recv(1024).decode()
		senha = input(msg)
		s.send(senha.encode())

		while True:
			print(s.recv(1024).decode())

			msg = input("> ")
			msg += "\n"

			s.send(msg.encode())

	def udp(ip, port):

		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		servidor = (ip, port)

		while True:
			msg = input ("> ")
			s.sendto(msg.encode(), servidor)

			dados, sys = s.recvfrom(1024)
			print(f"{sys} - {dados.decode()}")

