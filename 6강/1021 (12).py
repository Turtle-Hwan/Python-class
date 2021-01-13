# 실습 3
# 입력값 구구단의 단, 출력값 해당 구구

table = int(input("몇단? : "))

i=1     #제어변수
while (i <= 9):
    print(table, '*', i, '=', table*i)
    i = i + 1
