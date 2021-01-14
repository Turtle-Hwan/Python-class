#실습 3

def plus(start, end):
    s = 0
    for i in range(start, end + 1):
        s = s + i
    return s

value = plus(1, 10)

print(value)

value = plus(101, 110)

print(value)
