from multiprocessing import Queue


a = Queue(37)

print(a.empty())

a.put('abbbb')
print(a.empty())
print(a.qsize())


a.put('a')

print(a.empty())
print(a.qsize())

a.put('a')

print(a.empty())
print(a.qsize())

a.put('a')
print(a.empty())
print(a.qsize())


a.put('a')
print(a.empty())
print(a.qsize())


a.put('a')
print(a.empty())

a.put('a')
