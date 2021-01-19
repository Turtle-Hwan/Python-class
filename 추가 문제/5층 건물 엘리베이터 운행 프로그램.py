#5층 건물 엘리베이터 운행 프로그램

def goDown(now, target):
    for floor in range(now,target-1, -1):
        print("현재 층은 %d 입니다." %floor)
    print("%d 층에 도착하였습니다. 안녕히 가세요." %target)
def goUp(now, target):
    for floor in range(now, target+1, 1):
        print("현재 층은 %d 입니다." %floor)
    print("%d 층에 도착하였습니다. 안녕히 가세요." %target)

nowL = int(input("현재 층: "))
inputL = int(input("가는 층 입력: "))

if ((inputL == nowL) or (inputL < 1) or (5 < inputL)):
    print("다른 층(1~5)을 눌려주세요.")
else:
    if (nowL > inputL):
        goDown(nowL, inputL)
    else:
        goUp(nowL, inputL)
