# https://school.programmers.co.kr/learn/courses/30/lessons/161989
# 덧칠하기

def solution(n, m, section):
    result = 0 # 결과값 저장할 곳
    nsection = [] # 벽 공간 인덱스로 표현하기 위한 리스트
    
    for i in range(1,n+1):
        nsection.append(i)

    for i in range(0,len(nsection)):
        for j in range(0,len(section)):
            if nsection[i] == section[j]:
                nsection[i] = 0 # 덧칠해야 하는 구역 값 변경

    for i in range(m-1,len(nsection)+1):
        if nsection[i-m] == 0 and 0 in nsection[i-m:i]: #롤러를 다시 칠해야 하는 구간
            result += 1
    
    return result

n = 8
m = 4
section = [2, 3, 6]
print(solution(n,m,section))
