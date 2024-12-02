import socket

class Server:
	def udp(ip, port):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.bind(("0.0.0.0", port))

		print(f"Aguardando conexão UDP {ip} {port}")

		while True:
			dados, client = s.recvfrom(1024)
			print(f"{client} - {dados.decode()}")

			msg = input("> ")
			s.sendto(msg.encode(),client)

	def tcp(ip, port):

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((ip, port))
		s.listen(1)

		print(f"Aguardando conexão TCP {ip} {port}")
		con, client = s.accept()

		con.send("Digite a senha: ".encode())
		senha = con.recv(1024)

		if senha.decode() == "vascodagama":
			while True:
				msg = input("> ")

				if msg == "sair":
					s.close()
					break

				msg += "\n"

				con.send(msg.encode())

				dados = con.recv(1024)
				print(dados.decode())

		else:
			s.close()
