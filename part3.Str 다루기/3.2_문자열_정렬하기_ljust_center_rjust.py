# 문자열 정렬하기

'''
'가나다라                 ' # 좌측 정렬
'                 가나다라' # 우측 정렬
'        가나다라         ' # 가운데 정렬
'''

s, n = input().strip().split(' ')
n = int(n)

right_sort = s.ljust(n)
print(right_sort)

center_sort = s.center(n)
print(center_sort)

left_sort = s.rjust(n)
print(left_sort)
