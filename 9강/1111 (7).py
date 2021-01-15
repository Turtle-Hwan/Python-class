#실습 6

num = int(input("양수를 입력하세요 : "))

def printTo1(n):
    if (n==1):
        print(n)
    elif (n>=2):
        print(n)
        printTo1(n-1)

printTo1(num)
