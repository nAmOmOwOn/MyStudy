

# https://school.programmers.co.kr/learn/courses/30/lessons/120875


def solution(dots):

    '''
    (y2-y1)/(x2-x1)X  기울기

    '''
    m = []

    for i in range(0,len(dots)):
        for j in range(1,len(dots)):
            if i == j:
                pass
            elif i < j:
                m.append((dots[i][1] - dots[j][1]) / (dots[i][0] - dots[j][0]))

    if len(m) == len(set(m)):
        return 0
    else:
        return 1
    
dots = [[1, 4], [9, 2], [3, 8], [11, 6]]

print(solution(dots))