
def zz(self,x):
	print("zz")

	return x

def qq(self):
	print("qq")
def redoer(name,father, attr):

	dd = 3
	new_attr = {}

	new_attr['a'] = dd
	new_attr['zz'] = zz
	new_attr['qq'] = qq


	return type(name, father,new_attr)

class abc(object, metaclass= redoer):
	def __init__(self):
		self.n = 100
#	__metaclass__ = redoer

	print('1')
	aaa = 2
	print(aaa)
	bbb = 4

n = abc()
print(n.a)
print(n.zz(10))
#n.qq()
#n.b()
#n.c()
