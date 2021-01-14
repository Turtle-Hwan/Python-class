#실습 10

width = 10
height = 20


def area(w, h):
    global result
    
    result = w*h
    return result

print('면적 = ', area(width, height))
print(result)
