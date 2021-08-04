# n진법으로 적힌 문자열을 10진법으로 바꾸기

num, base = map(int, input().strip().split())
num = str(num)

answer = 0
for idx, number in enumerate(num[::-1]):
    answer += int(number) * (base ** idx)

print(answer)
