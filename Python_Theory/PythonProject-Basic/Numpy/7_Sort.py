import numpy as np

arr = np.random.randn(5,3)
print(arr)
arr.sort(1) # sort() 안의 값 = 넘긴 축의 값에 따라 1차원 부분을 정렬함
print(arr) 
print()

names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
print(np.unique(names)) # 중복된 원소 제거하고 남은 원소를 정렬된 형태로 반환 = sorted(set(names)) 와 같음
print()

values = np.array([6,0,0,3,2,5,6])
print(np.in1d(values, [2,3,6])) # 첫 번째 배열의 원소가 두 번째 배열의 원소를 포함하는지 True, False 로 나타냄
print()

x = np.array([1, 2, 3, 4])
y = np.array([3, 4, 6, 5])
print(np.intersect1d(x, y)) # 교집합
print(np.union1d(x, y)) # 합집합
print()

