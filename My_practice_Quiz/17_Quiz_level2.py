# https://school.programmers.co.kr/learn/courses/30/lessons/132265

def solution(topping):

    cnt = 0

    for i in range(0,len(topping)):
        if len(set(topping[0:i])) == len(set(topping[i:len(topping)])):
            cnt += 1
            
    return cnt


topping = [1, 2, 3, 1, 4]

print(solution(topping))