import requests
res = requests.get("http://google.com")
# res2 = requests.get("http://nadocoding.tistory.com")

res.raise_for_status()  # 문제가 생기면 곧장 종료 시킴

print("응답코드 :", res.status_code) # 200 이면 정상 아니면 오류남
# print("응답코드 :", res2.status_code)

if res.status_code == requests.codes.ok: # requests.code.ok 의미는 200이란 뜻
    print("정상입니다")
else:
    print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)


with open("mygoogle.html", "w", encoding = "utf8") as f:
    f.write(res.text)