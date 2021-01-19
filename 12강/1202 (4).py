#실습 4

import queue

q = queue.Queue()
print(q.queue)

q.put(1)
q.put(2)
q.put(3)

print(q.queue)
print(q.qsize())

print(q.get())
print(q.get())

print(q.queue)
print(q.qsize())
