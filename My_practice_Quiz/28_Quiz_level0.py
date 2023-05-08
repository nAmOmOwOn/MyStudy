# https://school.programmers.co.kr/learn/courses/30/lessons/181868

my_string = "    programmers  "

a = my_string.split(" ")

simple = [v for v in a if v]
print(simple)