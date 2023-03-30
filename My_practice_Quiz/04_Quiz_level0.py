# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    result = []
    hap = 0
    for i in range(0,num):
        hap += i
    x = (total - hap)/num
    for i in range(0,num):
        result.append(int(x + i))
    return result

num = 4
total = 14

print(solution(num,total))

