'''
표준 입력으로 정수 n이 주어질 때,
별(*) 문자를 이용해 높이가 n인 삼각형을 출력
'''

n = int(input().strip())

for i in range(1, n + 1):
    print('*'*i)
