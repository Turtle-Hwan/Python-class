#실습 8

num1 = int(input("수1 입력: "))
num2 = int(input("수2 입력: "))

if (num1 > num2):
    big = num1
    small = num2
else:
    big = num2
    small = num1

print(small,"~",big, "까지의 합")

s = 0
while (big >= small):
    s = s + small
    small = small + 1

print(s)
