# https://school.programmers.co.kr/learn/courses/30/lessons/120863

def solution(polynomial):
    xcount = 0
    number = 0

    for i in range(0,len(polynomial)):
        if polynomial[i] == "x":
            xcount += 1

    for i in range(1,len(polynomial)):
        if polynomial[i].isdigit() == True:
            number += int(polynomial[i])
        elif polynomial[i-1].isdigit() == True and polynomial[i].isalpha() == True:
            xcount += int(polynomial[i-1])
            xcount -= 1

    if xcount == 1 and number == 0:
        return "x"
    elif number == 0:
        return str(xcount) + "x"
    else:
        return str(xcount) + "x + " + str(number)





