# Quiz) 사이트 별로 비밀번호를 만들어주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 → naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 → naver
# 규칙3 : 남은 글자 중 처음 세 자리 + 글자 갯수 + 글자 내 'e'의 갯수 + '!'로 구성
#                        (nav)                      (5)                   (1)             (!)

# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"
url1 = url[7:-4] #규칙1+2 naver
url2 = url1[:3] # 규칙3 nav
len(url1) # 규칙3 글자갯수
url1.count("e") # 규칙3 e의 갯수

password = str(url2) + str(len(url1)) + str(url1.count("e")) + "!" 
print(password)

# password = str(url2) + str(len(url1)) + str(url1.count("e")) + "!" #잊지말자!!
