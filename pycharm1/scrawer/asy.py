#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from multiprocessing import Pool
import os
import time


# 父进程在子进程返回结果之后再执行
def test2(val):
	print('进程pid = %d val = %s' % (os.getpid(), val))


# 子进程的任务
def test():
	print('进程池中一个进程pid = %d ppid = %d'
	      % (os.getpid(), os.getppid()))

	for i in range(3):
		print('======%d===' % i)
		time.sleep(1)

	return '这是子进程返回结果'


p = Pool(2)

#               test是让子进程完成任务，test2让子进程完成之后通知父进程执行
p.apply_async(func=test, callback=test2)

for i in range(5):
	print('父进程pid = %d 正在工作' % os.getpid())
	time.sleep(1)

p.close()

