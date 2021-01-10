#실습 4
#화씨온도를 섭씨온도로 변환/화씨온도 입력, 섭씨 출력

fahrenheit = int(input("화씨온도: "))

fToCelsius = (fahrenheit - 32)* 5 / 9

print("섭씨온도 =", fToCelsius)
