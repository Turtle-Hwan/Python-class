#과제
#1 부터 입력받은 수 사이 N의 배수 합

endNum = int(input("끝수 입력: "))
timesNum = int(input("배수 선택: "))

sum = 0
for i in range(timesNum, endNum+1, timesNum):
    print(i)
    sum = sum + i

print("1~%d까지 %d의 배수의 합 = %d"%(endNum, timesNum, sum))
