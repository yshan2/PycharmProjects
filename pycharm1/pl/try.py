import os
import time

def t1():
	for i in range(30):
		print("xxxx")
		time.sleep(1)

def t2():
	for i in range(30):
		print("yyyy")
		time.sleep(1)

print('before')
pid1= os.fork()
pid2 = os.fork()

print('pid1 = %d, pid2 = %d, pid = %d, ppid = %d'
      %(pid1,pid2,os.getpid(),os.getppid()))

