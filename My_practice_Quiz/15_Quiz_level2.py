# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):

    cnt = 0

    for i in range(sum(number), len(discount)+1):
        need_number = []
        for j in range(0,len(want)):
            need_number.append(discount[i-sum(number): i].count(want[j]))
        
        if number == need_number:
            cnt += 1
        else:
            pass
    
    return cnt

discount = ["banana", "banana", "banana", "banana",
             "banana", "banana", "banana", "banana", 
             "banana", "banana"]

number = [10]

want = ["apple"]

print(solution(want,number,discount))