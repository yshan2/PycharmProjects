import os
import threading

os.mkdir('./Test')
l = os.listdir('/usr/lib/python2.7')
m = 0
def copyy(n):
	global m
	path = '/usr/lib/python2.7/'+n
	f = open(path,'rb')
	w = open('./test/'+n,'wb')
	w.write(f.read())
	m+= 1
	print(n + ' is moved by %s. %d'%(os.getpid(),m))

# print(l)
nu = 0
for i in l:
	if i[-3:]=='.py':
		nu+=1
		# print(i)
		a=threading.Thread(target=copyy, args = (i,))
		a.start()
print(nu)
