#실습 7


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


number = [7, 15, 23, 50, 61]

print(bin_search(number, 61))
print(bin_search(number, 88))





'''
while (low <= high):
        mid = (low + high)//2
        if (key == a[mid]):
            return mid
        elif (key < a[mid]):
            high = mid - 1
        else:
            low = mid + 1    
''' 
