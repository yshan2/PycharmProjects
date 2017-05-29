import time
import threading

class t(threading.Thread):
	def run(self):
		for i in range(10):
			time.sleep(0)
			print('this is from %s , the %s'%(self.name, str(i)))
			m = mu.acquire()
			if m:
				print('do the job. ')
				mu.release()
				print('done')


mu = threading.Lock()


a = t()
b = t()
a.start()
b.start()
