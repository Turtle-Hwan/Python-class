#실습 6

phone = {'Kim': '123-4567', 'Park': '234-5678', 'Lee': '345-6789'}

#키로 값얻기
result = phone['Kim']
print(result)
print(phone)

#함수이용
result = phone.get('Park')
print(result)
print(phone)

#삭제
result = phone.pop('Park')
print(result)
print(phone)

#del
del phone['Lee']
print(phone)

print('Kim' in phone)

#다 삭제
phone.clear()
print(phone)
