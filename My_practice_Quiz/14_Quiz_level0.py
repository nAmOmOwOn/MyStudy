# https://school.programmers.co.kr/learn/courses/30/lessons/120924
# 등차, 등비수열 문제

def solution(common):
    if common[1] % common[0] and common[2] % common[1] == 0:
        return int(common[1]/common[0]*common[len(common)-1])
    else:
        return int(common[len(common)-1] + (common[1] - common[0]))

common = [1, 2, 3, 4]

print(solution(common))