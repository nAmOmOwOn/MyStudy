# https://school.programmers.co.kr/learn/courses/30/lessons/120862

def solution(numbers):

    totalresult = []

    for i in range(0,len(numbers)):
        for j in range(i+1,len(numbers)):
            totalresult.append(numbers[i]*numbers[j])

    return max(totalresult)

