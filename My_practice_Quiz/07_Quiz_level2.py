# 문자열 압축하기

# 문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하기.

# 입력 예시: aaabbcccccca

# 출력 예시: a3b2c6a1

# 풀이1
s = "aaaabbbcczzzza"

#초기값을 설정합니다.
result = s[0] #반복문 실행되는 동안 문자열 형태로 반환되는 결과들을 담을 변수
count = 0 #반복되서 나오는 문자 수만큼 카운팅되는 값을 담을 변수

for i in s:
    if i == result[-1]: #result변수 마지막 문자와 비교합니다. else에서 result변수에 값이 추가되기 때문에 마지막 문자[-1]와 비교.
        count += 1
    else:
        result += str(count) + i #마지막 글자와 i가 다를 경우 카운팅된 값을 문자열 형태로 result 변수 마지막에 추가 해주고 i를 마지막 문자로 추가합니다.
        count = 1
result += str(count) #결과들이 담긴 변수에 마지막으로 카운팅된 값을 문자열 형태로 추가합니다.

print(result)

# 이것도 못품..