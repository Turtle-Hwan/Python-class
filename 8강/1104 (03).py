#실습 2

'''
def plus():
    s = 0
    for i in range(10):
        s = s + i + 1
    print(s)

plus()
'''



def plus(start, end):
    s = 0
    for i in range(start, end + 1):
        s = s + i
    print(s)

plus(1, 10)

