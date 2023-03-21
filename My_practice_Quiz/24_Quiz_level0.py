# https://school.programmers.co.kr/learn/courses/30/lessons/120808

import math

def solution(numer1,denom1,numer2,denom2):

    result = []

    lcm = math.lcm(denom1,denom2) # 최소 공배수

    lcm_numerator = numer1*(lcm//denom1) + numer2*(lcm//denom2)

    result.append(lcm_numerator)
    result.append(lcm)

    return result
