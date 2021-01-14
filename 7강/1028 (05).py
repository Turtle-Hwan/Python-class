#실습 6

numList = list()

while True:
    num = int(input("입력(종료 시 엔터)> "))
    if (num < 0):
        break
    numList.append(num)



s = 0
for x in numList:
    print(x, end=" ")
    s = s + x
    
print("\n합 =", s)
