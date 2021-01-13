#실습 5
#입력받은 수부터 1까지 더함

number = int(input("수 입력: "))

s = 0
while (number > 0):
    s = s + number
    number = number - 1

print(s)
