a, b, c = input("강의시작 시간, 분, 강의 시간 입력>>").split()
A = int(a)
B = int(b)
C = int(c)

print(A+(B+C)//60, (B+C)%60)

