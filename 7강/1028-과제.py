#과제

classNum = int(input("반 수 입력: "))

studentNum = int(input("반별 학생 수 입력: "))


scoreSum = 0
totalSum = 0


for i in range(classNum):
    for j in range(studentNum):
        korean = int(input("\n국어 점수 입력: "))
        english = int(input("영어 점수 입력: "))
        scoreSum = korean + english
        totalSum = totalSum + scoreSum

        print("합 = %d, 평균 = %.2f" %(scoreSum, scoreSum/2))

    print()

print("총합 = %d, 과목당 평균 = %.2f" %(totalSum, totalSum/(classNum*studentNum*2)))
