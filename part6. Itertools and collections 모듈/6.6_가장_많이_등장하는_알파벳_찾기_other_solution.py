'''
표준 입력으로 문자열, mystr이 주어진다. 
mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성

input	    output
'aab'	    'a'
'dfdefdgf'	'df'
'bbaa'	    'ab'
'''


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1,2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = {}
for number in my_list:
    try:
        answer[number] += 1
    except KeyError:
        answer[number] = 1

print(answer[1])  # = 4
print(answer[3])  # = 3
print(answer[100])  # =  raise KeyError
