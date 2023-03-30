# https://school.programmers.co.kr/learn/courses/30/lessons/120884
# 치킨 쿠폰


def solution(chicken):
    bonus = chicken // 10
    chicken += bonus
    while True:
        if bonus >= 10:
            chicken += bonus // 10
            bonus = bonus // 10
        else:
            break
    return chicken // 10


chicken = 1081

print(solution(chicken))