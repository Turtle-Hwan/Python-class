#실습 3

a = [3,5,1,2,4]
print("정렬 전:", a)

for i in range(len(a)-1,0,-1):
    for j in range(i):
        if(a[j]>a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
    print(a)

print("정렬 후:", a)
