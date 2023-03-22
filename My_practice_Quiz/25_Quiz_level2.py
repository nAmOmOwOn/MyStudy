# https://school.programmers.co.kr/learn/courses/30/lessons/118667

def solution(queue1,queue2):

    sum = 0

    for x in queue1:
        sum += x

    for x in queue2:
        sum += x

    if sum % 2 != 0:
        return -1

    cnt = 0

    sum_of_queue1 = 0
    sum_of_queue2 = 0

    for x in queue1:
        sum_of_queue1 += x

    for x in queue2:
        sum_of_queue2 += x

    if max(queue1) > sum_of_queue1 + sum_of_queue2 - max(queue1):
        return -1
    elif max(queue2) > sum_of_queue1 + sum_of_queue2 - max(queue2):
        return -1


    while True:

        sum_of_queue1 = 0
        sum_of_queue2 = 0

        for x in queue1:
            sum_of_queue1 += x

        for x in queue2:
            sum_of_queue2 += x


        if sum_of_queue1 == sum_of_queue2:
            
            return cnt
            
        if sum_of_queue1 > sum_of_queue2:
            min1 = queue1.pop(0)
            queue2.append(min1)
            cnt += 1
        elif sum_of_queue2 > sum_of_queue1:
            min2 = queue2.pop(0)
            queue1.append(min2)
            cnt += 1
        elif max(queue1) > sum_of_queue1 + sum_of_queue2  - max(queue1):
            return -1
        elif max(queue2) > sum_of_queue1 + sum_of_queue2  - max(queue2):
            return -1
        



queue1 = [1, 1]

queue2 = [1, 5]

print(solution(queue1,queue2))