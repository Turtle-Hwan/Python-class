#0930 과제

#리스트

numbers = []
print(numbers)

numbers.append(1)
numbers.append(2)
print(numbers)

numbers.pop(0)
numbers.remove(2)
print(numbers)

numbers.clear()

#셋

numbers = set()
print(numbers)

numbers.add(1)
numbers.add(2)
numbers.add(3)
print(numbers)

numbers.remove(1)
numbers.discard(2)
numbers.pop()
print(numbers)

numbers.clear()

#튜플

numbers = ()
print(numbers)

fruit = ('apple', 'banana')
print(fruit.index('apple'))
print(fruit.index('banana'))

#딕셔너리

contacts = {}
print(contacts)

contacts['Kim'] = '12345'
print(contacts)

print(contacts['Kim'])

result = contacts.get('Kim')
print(result)

result = contacts.pop('Kim')
print(result)
print(contacts)

contacts.clear()
