#실습 2
'''
def factorial(n):
    if (n==1):
        return 1
    elif (n>=2):
        return n*factorial(n-1)

n = int(input("정수값 입력: "))

print("결과:", factorial(n))


def factorial(n):
    if (n==1):
        return 1
    else:
        return n*factorial(n-1)

n = int(input("정수값 입력: "))

print("결과:", factorial(n))
'''

def factorial(n):
    if (n==1):
        return 1
    return n*factorial(n-1)

n = int(input("정수값 입력: "))

print("결과:", factorial(n))
