'''
iterable으로 곱집합을 구하는 방법

예시) 두 스트링 'ABCD', 'xy' 의 곱집합은 Ax Ay Bx By Cx Cy Dx Dy 
'''
import itertools


# 일반적인 방법
iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for value1 in iterable1:
    for value2 in iterable2:
        for value3 in iterable3:
            print(value1, value2, value3)


# itertools.product() 사용
a = 'ABCD'
b = 'xy'
c = '1234'

print(list(itertools.product(a, b, c)))
