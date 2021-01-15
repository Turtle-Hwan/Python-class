#실습 3

def hello(count):
    if (count == 0):
        return
    print(count,', Hello World!')
    count -= 2
    hello(count)

hello(10)
