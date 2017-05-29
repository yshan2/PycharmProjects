
#def a():
	#print('a')
	#print(x)

def b():
	print('b')

def c():
	print('c')

def redoer(name,father, attr):

	dd = 2
	attr = {}

	attr['a'] = dd



	return type(name, father,attr)

class abc(object, metaclass= redoer):
	def __init__(self):
		self.n = 100
#	__metaclass__ = redoer
	print('1')

n = abc()
n.a()
#n.b()
#n.c()
