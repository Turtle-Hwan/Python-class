#실습 2

string = input("문자열 입력: ")

s = []
result = True

for i in range(len(string)):
    s.append(string[i])

for i in range(len(string)):
    if string[i] != s.pop():
        result = False

print("결과:", result)
