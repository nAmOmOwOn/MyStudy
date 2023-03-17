# 2. 구글 플레이 앱으로 들어가서 여러분이 원하는 아무 앱에 작성된 리뷰를 파이썬으로
# 불러와 보기 좋게 풀력하세요.

import requests
from bs4 import BeautifulSoup

URL = "https://play.google.com/store/apps/details"
param = {"id" : "com.supercell.brawlstars"}
response = requests.get(URL, params = param)
htmlCode = response.text

soup = BeautifulSoup(htmlCode, 'html.parser')

# appNameTag = soup.find_all("div", class_ = "qxNhq")
# appNameTag = appNameTag[0]
# appNameTag = appNameTag.find('span')
# appName = appNameTag.text

# print(f'이번에 리뷰를 가져올 앱은 {appName} 앱입니다.')



reviews = soup.find("div", class_ = "Jwxk6d")
reviews = reviews.find_all("div", class_ = "EGFGHd")

print(len(reviews))

for review in reviews:
    reviewTextTag = review.find('div', class_ = 'h3YV2d')
    reviewText = reviewTextTag.text
    
    print(reviewText)
