import socket
import sys

ip = "0.0.0.0"
porta = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, porta))
s.listen(1)
print (f"aguardando conexão {ip} {porta}")

con, cliente = s.accept()
print (f"conectado com {cliente}")

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
