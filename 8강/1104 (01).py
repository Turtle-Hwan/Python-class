#실습 11

def sub():
    s = '바나나!'
    print(s)

sub()




def sub():
    print(s)

s = '사과!'
sub()


###

def change():
    x = 5

x = 1
change()
print(x)


def change():
    global x
    x = 5

x = 1
change()
print(x)


###

def change():
    x = 5
    y = 6
    z = 7

x = 1
y = 2

change()

print(x)
print(y)
#print(z)


def change():
    global x
    x = 5
    y = 6
    global z
    z = 7

x = 1
y = 2

change()

print(x)
print(y)
print(z)
