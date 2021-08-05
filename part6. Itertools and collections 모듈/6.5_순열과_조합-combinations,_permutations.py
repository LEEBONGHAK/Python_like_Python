'''
숫자를 담은 일차원 리스트, mylist에 대해 mylist의 원소로 이루어진 모든 순열을 사전순으로 return

mylist	    output
[2, 1]	    [[1, 2], [2, 1]]
[1, 2, 3]	[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
'''

# itertools.permutation를 이용하면, for문을 사용하지 않고도 순열 구할 수 있음
import itertools

pool = ['A', 'B', 'C']
print(list(map(list, itertools.permutations(pool))))  # 3개의 원소로 수열 만들기
print(list(map(list, itertools.permutations(pool, 2))))  # 2개의 원소로 수열 만들기
print("\n")

print(list(map(''.join, itertools.permutations(pool))))
print(list(map(''.join, itertools.permutations(pool, 2))))
print("\n")


# 조합은 itertools.combinations를 사용해서도 가능. 사용법은 permutations와 비슷함
print(list(map(list, itertools.combinations(pool, 3))))
print(list(map(list, itertools.combinations(pool, 2))))
