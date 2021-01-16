#실습 1

a = list()
flag = 0

for i in range(5):
    num = int(input("수 입력: "))
    a.append(num)

print(a)


key = int(input("찾고자 하는 수? "))

for cnt in range(5):
    if (key == a[cnt]):
        print("탐색 위치:", cnt)
        flag = 1
        break
    
if (flag == 0):
    print("찾는 값 없음")
