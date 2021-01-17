#실습 2

'''
a = []
for i in range(5):
    num = int(input("리스트값:"))
    a.append(num)
'''


a = [15,11,1,3,8]
print("정렬 전:", a)

for i in range(len(a)-1):
    min = i
    for j in range(i+1,len(a)):
        if (a[j]<a[min]):
            min = j

    a[i], a[min] = a[min], a[i]
    print(a)

print("정렬 후:", a)
