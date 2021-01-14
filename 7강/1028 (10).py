#실습 11

num = int(input("숫자 입력: "))

for j in range(1, num+1):
    print(j, '의 약수:', end='')
    
    for i in range(1, j+1):
        if (j % i == 0):
            print(i, end=' ')
    print()
    
