'''
표준 입력으로 문자열, mystr이 주어진다. 
mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성

input	    output
'aab'	    'a'
'dfdefdgf'	'df'
'bbaa'	    'ab'
'''

import collections

my_str = input().strip()

confirm = collections.Counter(my_str)
print(confirm)
print("\n")

maximum = max(confirm.values())
result = filter(lambda x: x[1] == maximum, confirm.items())
answer = [key for key, value in result]

print(''.join(sorted(answer)))
