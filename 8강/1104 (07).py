#실습 7

def get_max(x, y):
    if (x>y):
        return x
    else:
        return y

a = int(input("정수1 입력: "))
b = int(input("정수2 입력: "))

print("큰 수 =", get_max(a, b))
