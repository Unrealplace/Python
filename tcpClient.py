from socket import *

HOST = '192.168.199.231'
PORT = 21565
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSocket = socket(AF_INET,SOCK_STREAM)
tcpCliSocket.connect(ADDR)

while True:
	data = input('> ')
	if not data:
		break
	tcpCliSocket.send(bytes(data,'utf-8'))
	data = tcpCliSocket.recv(BUFSIZE)
	if not data:
		break
	print(data.decode('utf-8'))
	
tcpCliSocket.close()
