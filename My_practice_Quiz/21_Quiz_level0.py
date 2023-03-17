#https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):
    set_array = list(set(array))

    CntList = []

    for i in range(0,len(set_array)):
        cnt = 0
        for j in range(0,len(array)):
            if set_array[i] == array[j]:
                cnt += 1
        CntList.append(cnt)

    MaxCnt = []

    for i in range(0,len(CntList)):
        if max(CntList) == CntList[i]:
            MaxCnt.append(1)
            
    if len(MaxCnt) == 1 :
        return max(CntList)
    else:
        return -1

array = [1, 1, 2, 2]

print(solution(array))