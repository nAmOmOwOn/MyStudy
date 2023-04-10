strings = ["a","as","bat","car","dove","python"]

len_upper_2 = [x.upper() for x in strings if len(x) > 2]
print(len_upper_2)

unique_lengths = {len(x) for x in strings}
print(unique_lengths)
print(set(map(len,strings))) # map 함수를 이용해 위 unique_lengths 와 같이 만듬

loc_mapping = {index : val for index, val in enumerate(strings)}
print(loc_mapping)

some_tuple = [(1,2,3),(4,5,6),(7,8,9)]
flatter2 = [x for tup in some_tuple for x in tup]
print(flatter2)



