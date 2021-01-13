#실습 12

string = input("영문 문자열 입력: ")

for i in string:
    if i in 'aeiou':
        print(i, end=' ')
