#실습 14
userId = input("아이디: ")
userPassword = int(input("비밀번호: "))

if (userId != "apple"):
    print("로그인 실패\n아이디 불일치")
else:
    if (userPassword != 123):
        print("로그인 실패\n비밀번호 불일치")
    else:
        print("로그인 성공")
