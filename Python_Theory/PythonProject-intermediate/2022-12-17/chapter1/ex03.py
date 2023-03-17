import requests


# 네이버 영화 서비스에서 기생충 영화 정보를 파이썬으로 불러오세요
URL = "https://movie.naver.com/movie/bi/mi/basic.naver"
param = {"code" : "161967"}

response = requests.get(url = URL, params = param)

print(response)
print(response.text)

'''
requests, BeautifulSoup4
- 한계 :
        컴퓨터가 요청을 하는 것이기 때문에 반복문을 사용해서
        쉽게 불필요한 요청을 굉장이 하도록 조작할 수 있음
        그래서 서버 자체에서 requests로 한 요청은 응답하지 않도록 설정해둔 서버도 있음
        필요한 데이터가 상대적이라던가 특정 시점의 데이터라면 요청을 못할 수도 있음
'''

