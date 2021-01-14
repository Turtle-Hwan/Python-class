#실습 5

nameList = list()

while True:
    name = input("입력(종료 시 엔터)> ")
    nameList.append(name)

    if (name == ""):
        break

for x in nameList:
    print(x, end=" ")
