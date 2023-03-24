# 문제 : 

#     10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.

#     1000미만의 자연수에서 3,5의 배수의 총합을 구하라.


# 내 풀이
hap = [] 

for i in range(1, 1001):
    if i % 3 or i % 5 == 0:
        hap.append(i)
    
print(sum(hap))     

#추천수 높은 풀이
sum(list([x for x in range(1000) if x%3==0 or x%5==0]))