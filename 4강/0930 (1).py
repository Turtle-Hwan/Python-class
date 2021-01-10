#실습 1
fruits = {'apple', 'banana', 'pineapple'}
print(fruits)

print(sorted(fruits))

mySet = {1.0, 2.0, 'hello world', (1, 2, 3)}
print(mySet)


# set에서 원소로 들어간는 객체는 hashable 해야 함. 변경 불가능해야 함. (숫자, 문자열, 튜플)
'''
mySet = {1.0, 2.0, 'hello world', [1, 2, 3]}
mySet = {1.0, 2.0, 'hello world', {1, 2, 3}}
'''
