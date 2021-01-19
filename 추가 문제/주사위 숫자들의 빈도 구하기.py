#주사위 숫자들의 빈도 구하기

import random

counters = [0, 0, 0, 0, 0, 0]

for i in range(100):
    num = random.randint(0, 5)

    counters[num] += 1

for i in range(6):
    print("주사위 %d번의 빈도: %d" %(i+1, counters[i]))
