#실습 9

i=0
while (i<5):
    i = i + 1
    if (i == 3):
        break
    print(i)

i=0
while (i<5):
    i = i + 1
    if (i == 3):
        continue
    print(i)

i=1
while (i<5):
    if (i == 3):
        break
    print(i)
    i = i + 1

i=1
while (i<5):
    print(i)
    if (i == 3):
        continue
    i = i + 1
