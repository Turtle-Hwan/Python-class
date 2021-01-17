#실습 1

'''
a = [15, 11, 1, 3, 8]

min = 0

for i in range(min+1, 5):
    if (a[i] < a[min]):
        min = i

print("최솟값:", a[min])
print("인덱스:", min)
'''


a = [15, 11, 1, 3, 8]

print("교환 전:", a)

min = 0

for i in range(min+1, 5):
    if (a[i] < a[min]):
        min = i
        
'''
temp = a[0]
a[0] = a[min]
a[min] = temp
'''

a[min],a[0] = a[0],a[min]

print("교환 후:", a)
