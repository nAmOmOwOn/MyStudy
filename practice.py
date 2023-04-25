s = "banana"

result = []

lst = [x for x in s]

for x in range(len(s)):
    if lst[:x+1].count(lst[x]) == 1:
        result.append(-1)
    elif lst[:x+1].count(lst[x]) > 1:
        result.append(x - lst.index(s[x]))
        print(lst[x])
        print(lst.index(s[x]))
        lst[x - lst.index(s[x]) + 1] = 0

print(result)
print(lst)