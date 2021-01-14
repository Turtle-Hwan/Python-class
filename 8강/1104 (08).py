#실습 8

def get_max(x, y):
    if (x == y):
        return -1
    elif (x > y):
        return x
    else:
        return y

a = int(input("수1 입력: "))
b = int(input("수2 입력: "))

print(get_max(a,b))
