'''
파일 입출력 간단하게 하기
- 파일 입출력 코드를 간결하게 짜는 법
'''

# 일반적인 방법 - EOF를 만날 때까지, 파일 읽기를 반복
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    raw = line.split()
    print(raw)
f.close()
print('\n')


'''
파이썬에서는 파이썬의 with - as 구문을 이용하면 코드를 더 간결하게 이용
코드를 아래와 같이 쓰면 다음과 같은 장점이 존재

1. 파일을 close 하지 않아도 됩니다: with - as 블록이 종료되면 파일이 자동으로 close
2. readlines가 EOF까지만 읽으므로, while 문 안에서 EOF를 체크할 필요가 없음
'''
with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))

# with-as 구문은 파일 뿐만 아니라 socket이나 http 등에도 사용 가능
