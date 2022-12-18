import requests
from bs4 import BeautifulSoup

URL = "https://www.naver.com"
response = requests.get(URL)
htmlCode = response.text

result = BeautifulSoup(htmlCode, 'html.parser')
contents = result.find("a" , id_= "nav")
contentsList = result.find_all('a', class_="nav")
