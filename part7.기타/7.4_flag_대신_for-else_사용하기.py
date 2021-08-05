'''
자연수 5개가 주어지며,

1. 숫자를 차례로 곱해 나온 수가 제곱수1가 되면 found를 출력하고
2. 모든 수를 곱해도 제곱수가 나오지 않았다면 not found를 출력

예시 1          예시 2
입력            입력
2               5
4               1
2               2
5               3
1               1

출력            출력
found           not found
'''
from math import sqrt


# 풀이 1  - flag 변수 사용
numbers = [int(input()) for _ in range(5)]
check = 1
flag = True

for number in numbers:
    check *= number
    if sqrt(check) == int(sqrt(check)):
        flag = False
        print("found")
        break

if flag:
    print("not found")

print("\n")


# 풀이 2 - for-else 문 사용
# 코드를 짧게 쓸 수 있고, 의미를 알아보기 쉽기 때문에 권장됨
numbers = [int(input()) for _ in range(5)]
check = 1

for number in numbers:
    check *= number
    if sqrt(check) == int(sqrt(check)):
        print("found")
        break
else:
    print("not found")
