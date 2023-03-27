# https://school.programmers.co.kr/learn/courses/30/lessons/172927

def solution(picks, minerals):
    tired = 0
    for i in range(1,len(minerals)):
        if 5*i < len(minerals):
            mine = minerals[5*(i-1):5*i]
            if mine.count("diamond") > mine.count("iron") or mine.count("stone"): # 각 케이스 따져줘야됨
                if picks[0] > 0: # 다이아몬드 곡괭이부터 써야됨 그래야지 피로도 적음
                    picks[0] = picks[0] - 1 # 다이아몬드 곡괭이 썼으면 1개 빼줌
                    tired += mine.count("diamond") + mine.count("iron") + mine.count("stone") # 피로도 계산식
                elif picks[0] == 0 and picks[1] > 0:
                    picks[1] = picks[1] - 1
                    tired += mine.count("diamond")*5 + mine.count("iron") + mine.count("stone")
                elif picks[1] == 0 and picks[2] > 0:
                    tired += mine.count("diamond")*25 + mine.count("iron")*5 + mine.count("stone")
            elif mine.count("iron") > mine.count("diamond") or mine.count("stone"):
                if picks[0] > 0:
                    picks[0] = picks[0] - 1
                    tired += mine.count("diamond") + mine.count("iron") + mine.count("stone")
                elif picks[0] == 0 and picks[1] > 0:
                    picks[1] = picks[1] - 1
                    tired += mine.count("diamond")*5 + mine.count("iron") + mine.count("stone")
                elif picks[1] == 0 and picks[2] > 0:
                    picks[2] = picks[2] - 1
                    tired += mine.count("diamond")*25 + mine.count("iron")*5 + mine.count("stone")
            elif mine.count("stone") > mine.count("iron") or mine.count("diamond"):
                if picks[0] > 0:
                    picks[0] = picks[0] - 1
                    tired += mine.count("diamond") + mine.count("iron") + mine.count("stone")
                elif picks[0] == 0 and picks[1] > 0:
                    picks[1] = picks[1] - 1
                    tired += mine.count("diamond")*5 + mine.count("iron") + mine.count("stone")
                elif picks[1] == 0 and picks[2] > 0:
                    picks[2] = picks[2] - 1
                    tired += mine.count("diamond")*25 + mine.count("iron")*5 + mine.count("stone")
        else:
            mine = minerals[5*(i-1):len(minerals)]
            if mine.count("diamond") > mine.count("iron") or mine.count("stone"):
                if picks[0] > 0:
                    picks[0] = picks[0] - 1
                    tired += mine.count("diamond") + mine.count("iron") + mine.count("stone")
                elif picks[0] == 0 and picks[1] > 0:
                    picks[1] = picks[1] - 1
                    tired += mine.count("diamond")*5 + mine.count("iron") + mine.count("stone")
                elif picks[1] == 0 and picks[2] > 0:
                    picks[2] = picks[2] - 1
                    tired += mine.count("diamond")*25 + mine.count("iron")*5 + mine.count("stone")
            elif mine.count("iron") > mine.count("diamond") or mine.count("stone"):
                if picks[0] > 0:
                    picks[0] = picks[0] - 1
                    tired += mine.count("diamond") + mine.count("iron") + mine.count("stone")
                elif picks[0] == 0 and picks[1] > 0:
                    picks[1] = picks[1] - 1
                    tired += mine.count("diamond")*5 + mine.count("iron") + mine.count("stone")
                elif picks[1] == 0 and picks[2] > 0:
                    picks[2] = picks[2] - 1
                    tired += mine.count("diamond")*25 + mine.count("iron")*5 + mine.count("stone")
            elif mine.count("stone") > mine.count("iron") or mine.count("diamond"):
                if picks[0] > 0:
                    picks[0] = picks[0] - 1
                    tired += mine.count("diamond") + mine.count("iron") + mine.count("stone")
                elif picks[0] == 0 and picks[1] > 0:
                    picks[1] = picks[1] - 1
                    tired += mine.count("diamond")*5 + mine.count("iron") + mine.count("stone")
                elif picks[1] == 0 and picks[2] > 0:
                    picks[2] = picks[2] - 1
                    tired += mine.count("diamond")*25 + mine.count("iron")*5 + mine.count("stone")
    return tired

picks = [0, 1, 1]
minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]


print(solution(picks,minerals))
