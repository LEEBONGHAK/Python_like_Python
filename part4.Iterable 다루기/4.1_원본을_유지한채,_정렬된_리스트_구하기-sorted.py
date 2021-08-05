# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 deep copy와 sort 함수를 이용

import copy

list1 = [3, 2, 1]
print(f"list1 is {list1}")

list2 = [i for i in list1]  # 또는 copy.deepcopy를 사용
list2.sort()
print(f"list2 is {list2}")

list3 = copy.deepcopy(list1)
list3.sort()
print(f"list3 is {list3}\n")


# 더 좋은 사용법 -> sorted 사용 (복사와 정렬을 한번에)

list4 = [3, 2, 1]
print(f"list4 is {list4}")

list5 = sorted(list4)
print(f"list5 is {list5}")
