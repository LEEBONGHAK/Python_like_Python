'''
표준 입력으로 정수 n이 주어질 때,
별(*) 문자를 이용해 높이가 n인 삼각형을 출력
'''

n = int(input().strip())

answer= [123, 456] * n
print(answer)       # [123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, ...]


answer2 = 'abc' * n
print(answer2)      # abcabcabcabcabcabcabc ...  