# 알파벳 출력하기

import string

num = int(input().strip())

if num == 0:
    print(string.ascii_lowercase)   # 소문자 abcdefghijklmnopqrstuvwxyz
elif num == 1:
    print(string.ascii_uppercase)   # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ


# 다른 것들
# 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters)
print(string.digits)                # 숫자 0123456789
