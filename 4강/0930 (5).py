#실습 5

student = {'철수', '영희', '길동', '심청', '춘향'}

late = {'철수', '영희', '길동'}

absence = {'철수', '심청', '춘향'}


addP = student - late - absence

penaltyP = late & absence

print("가산점 받는 학생 :", addP)
print("벌점 받는 학생 :", penaltyP)
