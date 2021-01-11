#실습 16
totalPrice = int(input("총금액: "))

if (totalPrice >= 10000):
    print("할인액: %d" %(totalPrice/10))
else:
    if (totalPrice >= 5000):
        print("할인액: %d" %(totalPrice/20))
    else:
        print("할인 안됨!")
