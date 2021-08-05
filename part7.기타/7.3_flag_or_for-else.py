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

check = 1

for i in range(5):
    a = int(input())
    check *= a
    if (sqrt(check) - int(sqrt(check))) == 0.0:
        print("found")
        break
else:
    print("not found")
