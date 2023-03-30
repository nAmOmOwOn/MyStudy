# https://school.programmers.co.kr/learn/courses/30/lessons/118666
# 성격 유형 검사하기

# 지표 번호	성격 유형
# 1번 지표	라이언형(R), 튜브형(T)
# 2번 지표	콘형(C), 프로도형(F)
# 3번 지표	제이지형(J), 무지형(M)
# 4번 지표	어피치형(A), 네오형(N)

# 1	매우 비동의 // 3
# 2	비동의      // 2
# 3	약간 비동의 // 1
# 4	모르겠음    // 0
# 5	약간 동의   // 1
# 6	동의        // 2
# 7	매우 동의   // 3

def solution(survey , choice):
    MyMBTI = ""

    MBTI = {
        "R" : 0, "T" : 0,

        "C" : 0, "F" : 0,

        "J" : 0, "M" : 0,

        "A" : 0, "N" : 0
    }
    for x in range(0,len(survey)):
        if choice[x] < 4:
            MBTI[survey[x][0]] += (4 - choice[x])
        elif choice[x] > 4:
            MBTI[survey[x][1]] += (choice[x] - 4) # 딕셔너리에 value 값 추가하기 위함

    if MBTI["R"] > MBTI["T"] :
        MyMBTI += "R"
    elif MBTI["R"] < MBTI["T"] :
        MyMBTI += "T"
    else:
        MyMBTI += "R"

    if MBTI["C"] > MBTI["F"] :
        MyMBTI += "C"
    elif MBTI["C"] < MBTI["F"] :
        MyMBTI += "F"
    else:
        MyMBTI += "C"

    if MBTI["J"] > MBTI["M"] :
        MyMBTI += "J"
    elif MBTI["J"] < MBTI["M"] :
        MyMBTI += "M"
    else:
        MyMBTI += "J"

    if MBTI["A"] > MBTI["N"] :
        MyMBTI += "A"
    elif MBTI["A"] < MBTI["N"] :
        MyMBTI += "N"
    else:
        MyMBTI += "A"
    
    return MyMBTI # 노가다식.. 정답 맘에 안듬

    # MyMBTI += 'R' if MBTI['R'] >= MBTI['T'] else 'T'  위 식 깔끔하게 정리... 
    # MyMBTI += 'C' if MBTI['C'] >= MBTI['F'] else 'F'  if 절 이렇게 쓰는 연습..
    # MyMBTI += 'J' if MBTI['J'] >= MBTI['M'] else 'M'
    # MyMBTI += 'A' if MBTI['A'] >= MBTI['N'] else 'N' 

survey = ["AN", "CF", "MJ", "RT", "NA"]

choice = [5, 3, 2, 7, 5]

print(solution(survey,choice))