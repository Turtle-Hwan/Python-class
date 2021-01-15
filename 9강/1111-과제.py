#과제

num = [10,20,30]

def sumOfList(n):
    if (len(n) == 0):
       return 0
    else:
        return n.pop() + sumOfList(n)

print(num)
print("합 =", sumOfList(num))

