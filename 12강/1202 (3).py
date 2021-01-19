#실습 3

def palindrome(word):
    s = []
    for i in word:
        s.append(i)
    for i in word:
        if i != s.pop():
            return False
    return True

str = input("문자열 입력: ")

if len(str) <= 1:
    print("문자열 길이가 짧음")
else:
    print(palindrome(str))
