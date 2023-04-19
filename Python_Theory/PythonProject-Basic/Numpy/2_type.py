import numpy as np

arr = np.array([1,2,3,4,5])
print(arr.dtype)

float_arr = arr.astype(np.float64)
print(float_arr.dtype) # int 자료형 float 로 변경

numeric_string = np.array(["1.25","9.6","42"], dtype=np.string_)
print(numeric_string.dtype)
string_arr = numeric_string.astype(float)
print(string_arr.dtype) # string 자료형 타입 float 로 변경
