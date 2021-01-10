#과제 1
#친구 리스트 작성

friends = []


print('---- 추가 ----')
friends.append('현우')
print('친구:', friends)
friends.append('준환')
print('친구:', friends)
friends.append('민준')
print('친구:', friends)
friends.insert(1, '지훈')
print('친구:', friends)
friends.insert(2, '우진')
print('친구:', friends)

print('\n---- 삭제 ----')
friends.pop()
print('친구:', friends)
friends.pop(2)
print('친구:', friends)
friends.pop(1)
print('친구:', friends)
