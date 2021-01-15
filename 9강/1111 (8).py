#실습 7

def f(n):
    if (n<3):
        return n
    else:
        return f(n-1) - f(n-2) + f(n-3)*2

print(f(5))
