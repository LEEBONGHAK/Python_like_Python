# 이진 탐색하기 - binary search

import bisect

# 일반적인 binary search 구현 및 사용


def maked_bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


my_list = [1, 2, 3, 7, 9, 11, 33]
print(maked_bisect(my_list, 3))
print('\n')


# 파이썬의 bisect.bisect 메소드를 사용하여 이진 탐색(binary search) 사용
my_list2 = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(my_list2, 3))  # index가 아닌 들어갈 위치 반환 


'''
bisect 사용시 주의점

기존 Binary Search는 찾고자 하는 key 값이 발견되지 않으면 -1을 리턴하지만
bisect 모듈들은 key값이 없으면 해당 key값이 들어갈 위치를 반환

따라서, 이진탐색 목적으로 사용 할 경우에는 아래와 같이 따로 추가적인 구현이 필요
'''


def b_s(ary, key):
    i = bisect.bisect(ary, key)
    return i - 1 if ary[i - 1] == key else -1


print(b_s(my_list2, 3))
