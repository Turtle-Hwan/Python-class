#실습 1


num = int(input("정수값 입력: "))

def factorial(n):
    fac = 1
    for i in range(1, num+1):
        fac = fac*i
    return fac

print("결과:", factorial(num))

'''
num = int(input("정수값 입력: "))

def factorial(n):
    fac = 1
    if (n==1):
        fac = 1
    elif (n>=2):
        for i in range(2, n+1):
            fac = fac*i
    return fac

print("결과 :", factorial(num))
'''
