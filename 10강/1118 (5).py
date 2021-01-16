#실습 5

a = []
flag = 0

for i in range(7):
    num = int(input("수 입력:"))
    a.append(num)
    
print(a)
key = int(input("찾고자 하는 수? "))



low = 0
high = len(a)-1

while (low <= high):
    mid = (low + high)//2
        if (key == a[mid]):
            print("탐색 위치:",mid)
            flag = 1
            break
        elif (key < a[mid]):
            high = mid - 1
        else:
            low = mid + 1
if flag == 0:
    print("찾는 값 없음")
