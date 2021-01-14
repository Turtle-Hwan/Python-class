#실습 13

main = ['샌드위치', '와플', '베이글']
sub = ['커피', '주스']

print("<메뉴>")

order = 1

for i in main:
    for j in sub:
        print(order, i, "+", j)
        order = order + 1
