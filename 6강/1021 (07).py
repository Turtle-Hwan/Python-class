#실습 11

num = int(input("수 입력: "))


s = 0
i = 1
while (i <= num):
    i = i + 1
    if (i % 3 != 0):
        continue
    else:
        print(i)
        s = s + i

print("1 ~", num, "까지의 3의 배수의 합 =", s)

