# https://school.programmers.co.kr/learn/courses/30/lessons/12945
    
def solution(n):
    a = [0,1]
    
    for i in range(0,n-1):
        pi = a[i] + a[i+1]
        a.append(pi)
    
    return a[n]%1234567

