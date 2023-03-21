# https://school.programmers.co.kr/learn/courses/30/lessons/120878

def solution(a, b):
    if b % 2 == 0 or b % 5 == 0:
        return 1
    elif a / b >= 1 and a % b == 0:
        return 1
    else:
        return 2