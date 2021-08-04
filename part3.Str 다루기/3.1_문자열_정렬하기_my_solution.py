# 문자열 정렬하기

'''
'가나다라                 ' # 좌측 정렬
'                 가나다라' # 우측 정렬
'        가나다라         ' # 가운데 정렬
'''

s, n = input().strip().split(' ')
n = int(n)

right_sort = ''
for i in range(n - len(s)):
    right_sort += ' '
right_sort += s

center_sort = ''
for i in range((n - len(s)) // 2):
    center_sort += ' '
center_sort += s
for i in range((n - len(s)) // 2):
    center_sort += ' '

left_sort = ''
left_sort += s
for i in range(n - len(s)):
    left_sort += ' '

print(f"{right_sort}\n{center_sort}\n{left_sort}")
