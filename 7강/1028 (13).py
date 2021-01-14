#실습 14
'''
table = int(input("몇 단?? "))

for i in range(9):
    print(table, "*", i+1, "=", table*(i+1))
    
'''

for table in range(2, 10):
    for i in range(9):
        print(table, "*", i+1, "=", table*(i+1))
    print()
