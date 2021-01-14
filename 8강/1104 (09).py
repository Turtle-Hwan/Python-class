#실습 9

def plus(num):
    num += 1
    return num

num = 5

plus(num)

print(num)



def plus(num):
    num += 1
    return num

num = 5

result = plus(num)

print(result)



def plus():
    global num
    num += 1


num = 5

plus()

print(num)



def plus(num):
    num += 1
    return num

num = 5

print(plus(num))
