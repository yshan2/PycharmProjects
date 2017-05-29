from multiprocessing import Process
import os,time

def ppp():
	for i in range(1,11):
		print(i)
		time.sleep(1)



p = Process(target = ppp, name ='python3', )
print("开始")
p.start()
p.join(0.1)
print("结束")
for i in 'abcdefghijklmnopqrstuvwxyz':
	print(i)
	time.sleep(1)



