# 타자 연습 게임

import random

word = ['cat', 'dog', 'rabbit', 'duck', 'dolphin', 'wolf', 'raccoon', 'monkey']
w = random.choice(word)
cnt = 0
answer = 0

print('타자 게임 시작')
while True:
    print('(종료 0) >', w)
    my = input()
    cnt += 1
    if my == '0':
        break
    elif my == w:
        print('맞음!!')
        answer += 1
        w = random.choice(word)
    else:
        print('오타! 다시 도전!')

print('맞은 개수: {}, 정답률: {:.1f}%'.format(answer, answer/cnt*100))
