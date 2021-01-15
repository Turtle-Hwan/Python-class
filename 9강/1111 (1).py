#실습 9

def p(n):
    if (len(n) < 2):
        return True
    elif (n[0] == n[-1]):
        return p(n[1:len(n)-1])
    else:
        return False


str = input("문자열 입력: ")

if (len(str)<=1):
    print("문자열 길이가 짧음")
elif (p(str) == True):
    print("%s: 회문임" %str)
else:
    print("%s: 회문 아님" %str)
                
