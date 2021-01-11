#과제
month = int(input("월 입력: "))

if (month == 2):
    print("28일, 29일(윤년)")
elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    print("31일")
elif (month == 4 or month == 6 or month == 9 or month == 11):
    print("30일")
else:
    print("1 ~ 12 사이의 숫자를 입력해 주세요.")
