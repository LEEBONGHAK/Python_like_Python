'''
두 변수의 값을 바꾸는 방법 ( swap )

예시) a = 3, b = 'abc'를 a = 'abc', b = 3 으로 바꾸기
'''

# 일반적인 방법
a = 3
b = 'abc'
print(f"Before swap = a: {a}, b: {b}")

temp = a
a = b
b = temp
print(f"After swap = a: {a}, b: {b}")
print('\n')


# easy way in Python
c = 3
d = 'abc'
print(f"Before swap = c: {c}, d: {d}")

c, d = d, c
print(f"After swap = c: {c}, d: {d}")
