# 완전수 구하기

# 자기 자신을 제외한 모든 양의 약수들의 합이 자기 자신이 되는 자연수를 완전수라고 한다. 

# 예를 들면, 6과 28은 완전수이다. 6=1+2+3 // 1,2,3은 각각 6의 약수 28=1+2+4+7+14 // 1,2,4,7,14는 각각 28의 약수

# 입력으로 자연수 N을 받고, 출력으로 N 이하의 모든 완전수를 출력하는 코드를 작성하라


# 답 1
num= int(input("숫자를 입력하시오 : "))
print([x for x in range(1, num+1) if x==sum(y for y in range(1, x) if x%y==0)])


# 답2
N = int(input("Input a natural number: ")) # 숫자를 하나 입력합니다. 

result = [] # 완전수를 저장할 리스트.

for i in range(1, N+1): # 1부터 입력한 숫자까지
    sum = 0
    for j in range(1, i): # 1부터 i까지
        if i%j==0:  
            sum += j # 약수들의 합을 구합니다.

    if i == sum: # 자신을 제외한 약수들의 합이 자신과 같으면, 즉 완전수면.. 
        result.append(i)

print(result)

# 난 못품.. for 안의 for 감이 잘 안잡힘..