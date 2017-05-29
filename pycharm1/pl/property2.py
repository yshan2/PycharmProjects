class n:
	@property
	def num(self):
		return self.__num

	@num.setter
	def num(self,m):
		self.__num = m

a = n()
a.num = 333
print (a.num)