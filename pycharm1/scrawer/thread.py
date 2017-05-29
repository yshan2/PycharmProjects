import threading

# 创建全局ThreadLocal对象:
# local_school = threading.local()

def process_student(student):
    # 获取当前线程关联的student:
    std = student#local_school.
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
    print(threading.currentThread())
    print(threading.enumerate())
    # print(threading)

def process_thread(name):
    # 绑定ThreadLocal的student:
    student = name #local_school.
    process_student(student)

t1 = threading.Thread(target= process_thread, args=('dongGe',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('老王',), name='Thread-B')
print(threading.main_thread())
t1.start()
t2.start()
t1.join()
t2.join()