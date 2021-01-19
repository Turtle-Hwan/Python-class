# 커피숍 음료 주문 프로그램

menu = '''
<메뉴>
1. 아메리카노 3000원
2. 카페라떼 3500원
3. 카페모카 3800원
4. 종료
'''

print(menu)
sum = 0
discount = 0

while True:
    choice1 = int(input("번호 선택: "))

    if choice1 == 1:
        price = 3000
    elif choice1 == 2:
        price = 3500
    elif choice1 == 3:
        price = 3800
    elif choice1 == 4:
        break
    else:
        print("다시 입력하세요")
        continue

    choice2 = int(input("몇 잔?: "))
    total = price*choice2
    sum += total

if sum >= 20000:
    discount = sum*0.1
if sum != 0:
    print("\n총액 : %d원" % sum)
    print("할인액 : %d원" % discount)
    print("결제액 : %d원" % (sum-discount))
