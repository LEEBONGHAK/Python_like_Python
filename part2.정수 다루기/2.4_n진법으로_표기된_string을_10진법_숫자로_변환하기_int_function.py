# n진법으로 표기된 문자열(string)을 10진법으로 변환 하기
num, base = map(int, input().strip().split())
num = str(num)

answer = int(num, base)
print(answer)
