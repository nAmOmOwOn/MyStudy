# https://school.programmers.co.kr/learn/courses/30/lessons/152995

# 인사고과

def solution(scores):
    for i in range(len(scores)):
        for j in range(len(scores)):
            if scores[i][0] < scores[j][0] and scores[i][1] < scores[j][1]:
                scores[i][0], scores[i][1] = -1,-1
            
    for i in range(len(scores)):
        if -1 in scores[0]:
            return -1  # 만약 첫번째 사람이 인센티브를 못받는 경우
        elif -1 in scores[i]:
            scores.pop(i) # 아닌 경우 순위에서 제외시키기

    Sum_list = [] # 각 스코어의 점수 합을 리스트로 정렬

    for i in range(len(scores)):
        Sum_list.append(scores[i][0] + scores[i][1]) 

    grade = 1 # 첫 순위 설정
    while True:
        NumberOne = max(Sum_list)
        cnt = 0 # 중복등수 더할 변수를 설정함.
        for i in range(len(Sum_list)):
            if NumberOne == Sum_list[i]:
                Sum_list[i] = grade
                cnt += 1
        grade += cnt # 현재 등수 + 중복 등수 계산식

        if cnt == 1: # 중복 등수가 없는 경우
            break
    
    return Sum_list[0]


scores = [[2,2],[1,4],[3,2],[3,2],[2,1]]

print(solution(scores))