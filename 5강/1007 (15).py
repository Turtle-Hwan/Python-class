#실습 15
userId = input("아이디: ")
userPassword = input("비밀번호: ")

if (len(userId) >= 7):
    print("가입 실패\n아이디 글자수 초과")
else:
    if (len(userPassword) >= 7):
        print("가입 실패\n비밀번호 글자수 초과")
    else:
        print("가입 성공")
