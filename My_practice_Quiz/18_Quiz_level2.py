# https://school.programmers.co.kr/learn/courses/30/lessons/12911


def solution(n):

    i = 1

    while True:
        if str(bin(n)[2:]).count("1") == str(bin(n+i)[2:]).count("1"):
            return n+i
            break
        else:
            i += 1


