#실습 5

index = int(input("번호(인덱스) 입력: "))

def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

for i in range(index + 1):
    print('fibonacci(%d) = %d' %(i, fibonacci(i)))
