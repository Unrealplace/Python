from socket import *
from time 	import ctime

HOST = ''
PORT = 21565
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
	print('waiting for connecting....')
	tcpCliSock,addr = tcpSerSock.accept()
	if tcpCliSock and addr:
		print('....connected from :',addr)
		pass
	while True:
		data = tcpCliSock.recv(BUFSIZE)
		if not data:
			break
		print('[我是客户端发来的消息--->%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8')
		tcpCliSock.send(bytes('[我是服务器发的消息--->%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))
		pass
	tcpCliSock.close()
	pass
tcpSerSock.close()
pass