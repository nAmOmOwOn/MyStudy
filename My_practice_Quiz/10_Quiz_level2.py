# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    cnt = 0
    nsection = []
    
    for i in range(1,n+1):
        nsection.append(i)

    for i in range(0,len(nsection)):
        for j in range(0,len(section)):
            if nsection[i] == section[j]:
                nsection[i] = 0

    for i in range(m-1,len(nsection)+1):
        if nsection[i-m] == 0 and 0 in nsection[i-m:i]:
            cnt += 1
    
    return cnt
