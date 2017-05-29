import socket
from threading import Thread


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
addr = ('',19998)

s.bind(addr)
print('start')
paddr = 0


def rec(s):
	global paddr
	f = True
	while f:
		try:
			inf= s.recv(1024)
			# print(inf)
			print(inf.decode('gbk'))
			if inf == b'':
				break
		except OSError as e:
			print('exited')
			break
	s.close()

def send(s):
	global paddr
	while True:
		try:
			inf = input('what do you wanna say: ')
			if len(inf) == 0 :
				# s.close()
				break

			else:
				s.send(inf.encode('gbk'))

		except Exceptions:
			break
	s.close()

# while True:
s.listen(10)


try:
	while True:
		ss,caddr = s.accept()
		print(ss)
		print(caddr)

		t = Thread(target=rec, args=(ss,))

		t2 = Thread(target = send, args = (ss,))
		t2.start()
		t.start()
# while True:
# 	send = input('what to say: ')
# 	if len(send) == 0:
# 		print('you left.')
# 		s.close()
# 		break
# 	else:
# 		s.sendto(send.encode('gbk'),paddr)
# 		t.join()
# 		t2.join()
finally:
	s.close()
