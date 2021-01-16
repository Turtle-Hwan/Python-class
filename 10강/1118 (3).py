#실습 3

def seq_search(a, key):
    result = list()
    
    for i in range(len(a)):
        if key == a[i]:
            result.append(i)
    return result


number = [15,23,61,50,7,61]

print(seq_search(number, 61))
print(seq_search(number, 88))
