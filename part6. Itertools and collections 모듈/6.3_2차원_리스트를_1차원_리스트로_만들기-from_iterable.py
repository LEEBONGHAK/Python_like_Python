'''
문자열을 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어짐
solution 함수가 mylist를 일차원 리스트로 만들어 return

input	                            output
[[1], [2]]	                        [1, 2]
[['A', 'B'], ['X', 'Y'], ['1']]	    ['A', 'B', 'X' ,'Y', '1']
'''

import itertools
from functools import reduce
import operator
import numpy


my_list = [[1, 2], [3, 4], [5, 6]]
print(my_list)


# 방법 1 - sum 함수
answer = sum(my_list, [])
print(answer)


# 방법 2 - itertools.chain
print(list(itertools.chain.from_iterable(my_list)))


# 방법 3 - itertools와 unpacking
print(list(itertools.chain(*my_list)))


# 방법 4 - list comprehension 이용
print([element for array in my_list for element in array])


# 방법 5 - reduce 함수 이용 1
print(list(reduce(lambda x, y: x + y, my_list)))


# 방법 6 - reduce 함수 이용 2
print(list(reduce(operator.add, my_list)))


# 방법 7 - numpy 라이브러리의 flatten 이용
'''
각 원소의 길이가 동일한 경우에만 사용 가능
[[1], [2]] 또는 [[1, 2], [2, 3], [4, 5]] -> OK
[['A', 'B'], ['X', 'Y'], ['1']] -> Not OK
'''
print(numpy.array(my_list).flatten().tolist())
