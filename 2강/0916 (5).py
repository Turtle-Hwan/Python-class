#실습 5
#형식지정자
number1 = int(input("숫자입력: ")) 
number2 = int(input("숫자입력: ")) 
sum = number1 + number2
print("합 =", sum)           

print("합 = %d" %sum)

#
division = number1 / number2
print("나눗셈 = ", division)
print("나눗셈 = %f" %division)
print("나눗셈 = %.3f" %division)
print("나눗셈 = %5.2f" %division)

#
capital = "서울"
print("대한민국의 수도: %s" %capital)

#
PI = 3.14159

print(PI)
print("%d" %PI)
print("%f" %PI)

print("%.2f" %PI)
print("%.4f" %PI)

print("%5d" %PI)
print("%5.2f" %PI)
