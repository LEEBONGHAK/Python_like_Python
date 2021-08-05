# Iterable의 모든 멤버의 type을 변환

list1 = ['1', '100', '33']
print(list1)

list2 = []
for value in list1:
    list2.append(int(value))
print(list2)
