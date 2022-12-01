
e_count = 0
num_count = 0

while(True):
    ID = input("ID를 입력하세요(3글자 이상)>>>")

    if len(ID) < 4:
        print("3글자 이상 입력해주세요")
        break

    PassWord = input("패스워드를 입력하세요(영문 숫자 포함 8자 이상)>>>")

    for i in PassWord:
        if i.isalpha():
            e_count +=1
        elif i.isnumeric():
            num_count +=1
    if e_count > 0 and num_count > 0:
        pass
    if len(PassWord) < 8:
        print(">영문 숫자 포함 8자 이상 입력해주세요!")
        break

    PassWordc = input("패스스워드 확인 한번 더 입력하세요>>>")
    if PassWord != PassWordc:
        print(">일치하지 않습니다! 다시 입력해주세요!")
    else:
        print("회원가입이 완료되었습니다.")
    break
            
print("로그인 화면~")

while(True):    
    LID = input("ID를 입력하세요>>>")
    if LID != ID:
        print(">아이디가 일치하지 않습니다.")
        continue
    break

while(True):                                                 
    LPassWord = input("패스워드를 입력하세요>>")
    if LPassWord != PassWord:
        print("패스워드가 일치하지 않습니다.")
        continue
    break
        
print("로그인 성공!! \n {0}님 환영합니다.".format(ID))

            
                