'''
문자열 리스트 mylist를 입력받아, 이 리스트의 원소를 모두 이어붙인 문자열을 return 

예를 들어 mylist가 ['1', '100', '33'] 인 경우, solution 함수는 '110033'을 return
'''

my_list = ['1', '100', '33']
print(my_list)

answer = ''.join(my_list)
print(answer)
