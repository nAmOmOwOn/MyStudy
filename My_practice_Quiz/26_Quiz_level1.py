#https://school.programmers.co.kr/learn/courses/30/lessons/133502
# 햄버거 만들기
def solution(ingredient):

    cnt = 0
    try:
        while True:
            if len(ingredient) < 4:
                return cnt

            for i in range(0,len(ingredient)):
                if ingredient[i] == 1 and ingredient[i+1] == 2 and ingredient[i+2] == 3 and ingredient[i+3] == 1:
                    ingredient.pop(i)
                    ingredient.pop(i)
                    ingredient.pop(i)
                    ingredient.pop(i)
                    cnt += 1
                    break

    except:
        cnt = 0
        return cnt

ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]

print(solution(ingredient))

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]

print(solution(ingredient))