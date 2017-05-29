from multiprocessing import Process
import os

def process1(*args):
	print('a')
	print(os.getpid())
	print(args)

print(os.getpid())
p = Process(target=process1,name='what?',args=(1,2))
p.start()
print('b')
p.join()

