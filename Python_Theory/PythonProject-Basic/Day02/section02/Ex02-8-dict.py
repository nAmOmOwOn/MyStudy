'''
파일명 : Ex02-8-dict.py

Dictionary
    key:value 로 이루어져 쌍으로 데이터 값을 자정하는데 사용
'''
# dictionary 선언
thisdict = {
    "brand" : "구찌",
    "model" : "g001",
    "year" : 2022
}
print(thisdict)

'''
키 이름을 사용하여 참조할 수 있다.   
'''
#값 가져오기
thisdict = {
    "brand" : "구찌",
    "model" : "g001",
    "year" : 2022
}
print(thisdict["brand"])
print(thisdict.get("model"))

# 키 목록 가져오기
print(thisdict.keys())

# 추가하기
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict["color"] = "red"
print(thisdict)
thisdict.update({"bgColor" : "black"})
print(thisdict)

# 변경하기
thisdict["color"] = "yellow"
thisdict.update({"bgColor" : "blue"})
print(thisdict)

# 제거하기
thisdict.pop("model")
print(thisdict)

# 마지막 삽입된 항목 제거하기
thisdict.popitem()
print(thisdict)

words = ["apple","bat","bar","atom","book"]
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
print(by_letter)


words = ["apple","bat","bar","atom","book"]
by_letter = {}
for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)
print(by_letter)

from collections import defaultdict
words = ["apple","bat","bar","atom","book"]
by_letter = {}
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
print(by_letter)


