#실습 1

while True:
    number = int(input("수 입력: "))
    
    if (number == 0):
        print("종료")
        break

    elif (number % 2 == 1):
        print("홀수")
    else:
        print("짝수")
