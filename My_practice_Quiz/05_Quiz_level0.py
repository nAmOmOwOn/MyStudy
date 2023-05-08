# https://school.programmers.co.kr/learn/courses/30/lessons/120884
# 치킨 쿠폰

def solution(chicken):
    answer = 0
    coupon = chicken

    while coupon >= 10:
        eaten = coupon//10 
        answer += eaten 
        coupon = coupon%10 + eaten 
    return answer 

chicken = 1081

print(solution(chicken))