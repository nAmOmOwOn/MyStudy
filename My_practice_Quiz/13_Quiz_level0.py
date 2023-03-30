# https://school.programmers.co.kr/learn/courses/30/lessons/120866
# 안전지대

def solution(board):
    result = 0
    try:
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] == 1:
                    if board[i][j-1] == 0:
                        board[i][j-1] = "X"
                    if board[i][j+1] == 0:
                        board[i][j+1] = "X"
                    if board[i-1][j-1] == 0:
                        board[i-1][j-1] = "X"
                    if board[i-1][j] == 0:
                        board[i-1][j] = "X"
                    if board[i-1][j+1] == 0:
                        board[i-1][j+1] = "X"
                    if board[i+1][j-1] == 0:
                        board[i+1][j-1] = "X"
                    if board[i+1][j] == 0:
                        board[i+1][j] = "X"
                    if board[i+1][j+1] == 0:
                        board[i+1][j+1] = "X"
    except IndexError:
        pass

    for i in range(0,len(board)):
        result += board[i].count(0)

    return result

board = [[0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0], 
         [0, 0, 1, 1, 0], 
         [0, 0, 0, 0, 0]]

print(solution(board))