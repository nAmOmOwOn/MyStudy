# https://school.programmers.co.kr/learn/courses/30/lessons/131704

def solution(order):
    pickup = []

    another = []

    number = 1

    for i in range(0,len(order)):  
        if order[i] == number:
            pickup.append(order[i])
            order[i] = 0
            number += 1
        else:
            another.append(order[i])

    while(True):
        if len(another) == 0:
            break
        elif another[len(another)-1] == number:
            pickup.append(another[len(another)-1])
            another.pop()
            number += 1
        else:
            break
    return len(pickup)

order = [4, 3, 1, 2, 5]

print(solution(order))