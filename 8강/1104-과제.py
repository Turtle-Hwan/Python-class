#과제

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiple(x, y):
    return x*y

def div(x, y):
    if(y == 0):
        print("---0으로 나눌 수 없음---")
        return 'n/a'
    else:
        return x/y



a = int(input("숫자 입력: "))
b = int(input("숫자 입력: "))

print("\n덧셈 =", plus(a, b))
print("뺄셈 =", minus(a, b))
print("곱셈 =", multiple(a, b))
print("나눗셈 =", div(a, b))
