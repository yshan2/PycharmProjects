import threading
from time import sleep,ctime

def t1():
	for i in range(5):
		print('t1')
		sleep(1)

def t2():
	for i in range(5):
		print('t2')
		sleep(1)

print('start time'+ ctime())
m = threading.Thread(target=t1)
n = threading.Thread(target=t2)

m.start()
n.start()
while True:
	s = len(threading.enumerate())
	print('threads are %d'%s)
	sleep(0.5)
	if s<2:
		break


print('main done' + ctime())


