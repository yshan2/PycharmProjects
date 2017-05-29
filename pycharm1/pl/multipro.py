from multiprocessing import Process
import time,os

class theprocess(Process):
	def __init__(self,inter):
		Process.__init__(self)
		self.inter = inter

	def run(self):
		print('子进程（%s）开始执行，父进程（%s）'%(os.getpid(),os.getppid()))
		t_start= time.time()
		time.sleep(self.inter)
		t_end = time.time()
		print('%s time cost %0.2f'%(os.getpid(),(t_end-t_start)))

tstart= time.time()
print('%s start.'%os.getpid())
a = theprocess(4)
a.start()
a.join(2)
tstop = time.time()
print('%s stoped. '%os.getpid())
print('costed %.2f'%(tstop-tstart))
