# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    slist = []

    for x in range(0,len(s)):
        slist.append(s[x])
    cnt = 0
    while True:
        try:   
            if slist[cnt] == slist[cnt+1]:
                slist.pop(cnt)
                slist.pop(cnt)
                cnt = 0
            else:
                cnt += 1
            
            if len(slist) == 0:
                return 1
                break
        except IndexError:
            return 0
            break
        
s = "caca"

print(solution(s))