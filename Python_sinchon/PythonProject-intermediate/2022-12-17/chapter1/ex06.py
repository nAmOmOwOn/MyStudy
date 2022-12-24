# 1. 네이버 영화 페이지에 들어가자 마자 보이는 박스오피스 1위 ~ 10위 까지의 정보를
# 파이썬으로 불러와서 보기 좋게 출력해보세요.
# a) 라이브러리 설치 및 HTML기초 : 312 ~ 317 페이지
# b) 요청: 318 ~ 321 페이지
# c) 파싱 : 322 페이지(1)
# d) 컨텐츠 꺼내기 : 322페이지 (2) ~ 328페이지
# e) 컨텐츠가 가지고 있는 텍스트 꺼내기 : 323페이지 2-1의 태그 내용
# f) 컨텐츠가 가지고 있는 속성의 값 꺼내기 : 323페이지 2-1의 속성 값



import requests
from bs4 import BeautifulSoup

URL = "https://movie.naver.com"
response = requests.get(URL)
htmlCode = response.text

result = BeautifulSoup(htmlCode, 'html.parser')
# 주의 사항
# 나에게 필요한 정보가 시간에 따라서 자동으로 바뀌기 때문에 
# 파이썬으로 불러온 컨텐츠가 나에게 필요한 컨텐츠인지 확인을 해줘야 함
# 내가 보고있는 웹페이지랑 파이썬이 불러오는거랑 다를 수도 있다!!

items = result.find_all("li", class_="item")

for item in items:
    print(item.text)


for item in items:
    if "박스오피스" in item.text:
        print("개발자가 원하는 컨텐츠를 불러왔습니다")
