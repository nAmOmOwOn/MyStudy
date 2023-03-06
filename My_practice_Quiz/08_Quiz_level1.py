# https://school.programmers.co.kr/learn/courses/30/lessons/136798

def solution(number, limit, power):
    countsum = []
    result = 0
    for i in range(1,number+1):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
        countsum.append(count)

    for i in range(0,len(countsum)):
        if countsum[i] > limit:
            result += power
        else:
            result += countsum[i]
    return print(result)