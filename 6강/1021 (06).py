#실습 10
#1부터 입력받은 수 사이 3의 배수

num = int(input("수 입력: "))
print("1 ~", num, "까지의 3의 배수")

i = 1

while (i <= num):
    i = i + 1
    if (i % 3 != 0):
        continue
    else:
        print(i)



'''
num = int(input("수 입력: "))
print("1 ~", num, "까지의 3의 배수")

i = 1

while (i<=num):
    if (i%3) == 0:
        print(i)
    i = i + 1

'''
