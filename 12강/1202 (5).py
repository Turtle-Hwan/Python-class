#실습 5

import queue

q = queue.Queue()
print(q.queue)

q.put('사과')
q.put('딸기')
print(q.get())
print(q.queue)

q.put('포도')
print(q.get())

q.put('귤')
print(q.queue)
print(q.qsize())
