from multiprocessing import Process #,Queue
from queue import Queue

# from queue import Queue

# from queue import Queue

import os , time
# from queue import Queue
# from queue import Queue

# w = Queue()



class ppp(Process):
    def __init__(self):
        Process.__init__(self)

    def run(self):
        print('start')

        time.sleep(1)
        os.getpid()

        print('a is from %d'%os.getppid())
        print('a is %d'%os.getpid())

        print('b is borned from %d'%os.getppid())

        b = os.fork()

        y = os.getpid()
        w.put(b)
        print('b is %d' % b)
        print('b is %d' % os.getpid())
        print('b is borned from %d' % os.getppid())
        # print(os.numerate())


def ggg():
    print('1111')
    while True:
        rrr = w.get()
        #rrr = w.get(True)
        print('this is ggg')
        print(rrr)


w = Queue()
a = ppp()
a.start()
print('22222')
print('r is from %d'%os.getppid())
ttt= Process(target=ggg)
ttt.start()
# ttt.enumerate()
print('r is %d'%os.getpid())
print('done 1')
