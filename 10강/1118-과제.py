# 과제

def bin_search(a,key):
    low = 0
    high = len(a) - 1
    for i in range(len(a)):
        if (low <= high):
            mid = (low + high)//2
            if (key == a[mid]):
                return mid
                break
            elif (key < a[mid]):
                high = mid - 1
            else:
                low = mid + 1    
    return -1



num = int(input("몇 명? "))
name = list()

for i in range(5):
    name.append(input("입력: "))

print(name,'\n')


a = bin_search(name, input("찾고자 하는 이름? "))

if a == -1:
    print("찾는 이름이 없습니다.")
else:
    print(a+1, "번째에 이름이 있습니다")
    

