#실습 6

def circle(r):
    area = 3.14*r*r
    return area

radius = int(input("반지름 입력: "))

print('원의 넓이 =', circle(radius))
