#실습 7
credit = int(input("이수 학점 수? "))
grade = float(input("평점? "))

if (credit >= 140 or grade >= 3.0):
    print("졸업 가능합니다!")
else:
    print("졸업이 힙듭니다!")
