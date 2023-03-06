# https://school.programmers.co.kr/learn/courses/30/lessons/161990


def solution(wallpaper):
    # (row_min, col_min) (row_max, col_max)

    answer = []

    n = len(wallpaper)
    m = len(wallpaper[0])

    row_min = n
    col_min = m
    row_max = 0
    col_max = 0

    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == '#':
                row_min = min(i,row_min)
                col_min = min(j,col_min)
                row_max = max(i,row_max) 
                col_max = max(j,col_max) 

    answer =[row_min,col_min,row_max+1,col_max+1]
    return answer
