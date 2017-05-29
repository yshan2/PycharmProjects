import sys
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, SO_REUSEPORT

from multiprocessing import Process

import time

serv = socket(AF_INET, SOCK_STREAM)
# serv.setsockopt()
print(serv.getsockname())

serv.setsockopt(SOL_SOCKET,SO_REUSEPORT,1)
serv.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# time.sleep(1)
print(serv.getsockopt(SOL_SOCKET,SO_REUSEPORT))
print(serv.getsockopt(SOL_SOCKET,SO_REUSEADDR))
# servaddr= ('',9996)
serv.bind(('',9995))
serv.listen(10)
print('listening.')


def recev(soc):
	rec = soc.recv(1024)
	print(rec.decode('gbk'))

	recHead = rec.decode('gbk').splitlines()
	print(recHead)

	#response
	rStatus = 'HTTP/1.1 200 OK\r\n'
	rheader = 'Contend-Type = text/Plain\r\n'
	rbody = 'hello'

	response = rStatus+rheader+'\r\n'+rbody
	soc.send(response.encode('gbk'))

	soc.close()
	pass



while True:
	actserv,cliaddr = serv.accept()
	print('connected')
	# actserv.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

	p = Process(target=recev,args=(actserv,))
	p.start()
	actserv.close()







