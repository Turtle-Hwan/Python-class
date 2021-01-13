#실습 13

num = int(input("정수 입력: "))

fac = 1
for i in range(num):
    fac = fac*(i+1)

print(num, "! =", fac)
