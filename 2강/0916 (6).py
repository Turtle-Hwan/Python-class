#실습 6
#초 입력, 시 분 초 출력

sec = int(input("초 단위 시간: "))

hour = sec//3600
min = sec%3600//60
sec = sec%60

print("%d시간 %d분 %d초" %(hour, min, sec))
