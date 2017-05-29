import os
a = os.fork()

while True:
	if a == 0:
		print('world %d'%a)
	else:
		print('hello %d'%a)

