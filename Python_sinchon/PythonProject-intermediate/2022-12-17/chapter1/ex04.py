import requests
from bs4 import BeautifulSoup

URL = "https://www.naver.com"
response = requests.get(URL)
htmlCode = response.text

result = BeautifulSoup(htmlCode, 'html.parser')

'''
find(찾고자 하는 컨텐츠의 경로) : 찾고자 하는 컨텐츠 중에서 첫 번째 컨텐츠를 찾아주는 함수
find_all(찾고자 하는 컨텐츠의 경로) : 찾고자 하는 컨텐츠를 전부 찾아주는 함수

find 함수를 사용해서 컨텐츠를 찾으면 bs4.element.Tag 타입의 태그를 가지고 있는 객체가 반환됨

find_all 함수를 사용해서 컨텐츠들을 찾으면 bs4.element.Tag 타비의 태그글 가지고 있는 객체 리스트가 반환됨

'''

contents_list = result.find_all('a')

# 반복문과 contents_list를 사용해서 찾은 모든 a태그를 화면에 출력하세요.
# 1. contents_list에 들어있는 데이터 유형을 파악한다.(유형에 맞춰서 활용할 수 있기때문)
# print(type(contents_list[0]))

# firstContents = contents_list[0]
# print(firstContents)
# print(firstContents.text)

# a태그에 "메일" 이 포함된 태그가 몇번째 태그에 있는지?

count = 0
for n in contents_list:
    nthTagText = n.text
    count += 1
    if nthTagText.find("메일") != -1:  # 강사님 풀이
        print(count)

count = 0
for n in contents_list:
    nthTagText = n.text
    count += 1
    if "메일" in nthTagText:  # 내 풀이, count는 생각을 못함..
        print(count)


print(contents_list[40])
classAttr = contents_list[40].get("class")
hrefAttr = contents_list[40].get("href")

print(f"메뉴 버튼의 class 속성의 값 = {classAttr}")
print(f"메뉴 버튼의 href 속성의 값 = {hrefAttr}")

'''
bs4.element.Tag 타입 객체
-> text 맴버 변수 : 그 태그가 가지고 있는 텍스트 컨텐츠를 반환
-> get() 함수 : 그 태그가 가지고 있는 특정한 속성값을 반환
'''