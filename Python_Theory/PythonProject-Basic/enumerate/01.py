'''
파일명 : Ex09-3-enumerate.py
enumerate()
    List, Tuple, String 등 자료형을 입력받으면
    인덱스 값을 포함하는 enumerate 객체를 돌려준다.
'''
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(type(enumerate(months)))
for month, day in enumerate(months):
    print('{}월 = {}일'.format(month+1, day))

some_list = ['foo', 'bar', 'baz']
mapping = {}
for i ,v in enumerate(some_list):
    mapping[i] = v
print(mapping)

some_list2 = ['foo', 'bar', 'bas']
mapping2 = {}
for i,v in enumerate(some_list2):
    mapping2[v] = i
print(mapping2)

strings = ["a","as","bat","car","dove","python"]
loc_mapping = {index : val for index, val in enumerate(strings)}
print(loc_mapping)