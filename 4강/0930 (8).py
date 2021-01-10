#실습 8

str = 'Where there is a will, there is a way'
print(type(str))

result = str.split()
print(result)
print(type(result))
print(len(result))

print(str)


print('\n\n')


#+
str = 'Where there is a will, there is a way'
print(type(str))

result = str.split(',')
print(result)
print(type(result))
print(len(result))

print(str)


print('\n\n')


#++
str = 'Where there is a will, there is a way'

result = str.replace('w', 'T')
print(result)

print(str)

print('w' in str)

print(str.count('i'))




