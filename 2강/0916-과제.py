#과제 1
#과목별 점수 입력, 총점 평균(소수점둘째) 출력

sub1 = int(input("첫번째 과목 점수: "))
sub2 = int(input("두번째 과목 점수: "))
sub3 = int(input("세번째 과목 점수: "))

sum = sub1 + sub2 + sub3

average = sum/3

print("총점:", sum)
print("평균: %.2f" %average)
