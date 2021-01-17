#과제 1 선택정렬 내림차순

a = [15,11,1,3,8]

print("정렬 전:", a)

for i in range(len(a)-1):
    max = i
    for j in range(i+1,len(a)):
        if (a[j] > a[max]):
            max = j

    a[i], a[max] = a[max], a[i]
    print(a)

print("정렬 후:", a)
