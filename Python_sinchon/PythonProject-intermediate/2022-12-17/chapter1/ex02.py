import requests

URL = "https://search.naver.com/search.naver"
params = {'query' : '파이썬','sm' : 'tab_hty.top','where': 'nexearch'}

response = requests.get(url = URL, params = params)

print(response)
print(response.text)

'''
200번 코드로 응답이 왔다고 해서 내가 원하는 결과가 안나올 수도 있음
'''

'''
요청 하는 방법
1. requests 라이브러리 import
2. requests.get(URL, PARAMETER)
3. get 함수가 반환해주는 결과값을 변수에 저장
4. 변수를 그대로 출력해서 응답코드를 확인
5. text 맴버 변수를 출력해서 결과값을 확인 또는 활용
'''

