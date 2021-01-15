#실습 8

def p(n):
    for i in range(int(len(n)/2)):
        if (n[i] != n[len(n)-1-i]):
            return False
            break
        if (i == int(len(n)/2)-1):
            return True

str = input("문자열 입력: ")

if (len(str)<=1):
    print("문자열 길이가 짧음")
else:
    print("결과:", p(str))
                
