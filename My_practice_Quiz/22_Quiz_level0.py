# https://school.programmers.co.kr/learn/courses/30/lessons/120878

def solution(a, b):
    if a == b :
        return 1
    elif b % 2 == 0 or b % 5 == 0:
        return 1
    elif b > a and b % a == 0:
        return 1
    elif a > b and a % b == 0:
        return 1
    else:
        return 2
    

print(77%7)