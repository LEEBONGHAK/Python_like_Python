'''
    solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.

    Ex)
    mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]일 경우 경우, 
    solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 return
'''

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(mylist)

new_list = list(map(list, zip(*mylist)))
print(new_list)


'''
zip(iterables)
- Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

Example #1 - 일반적인 사용법

mylist = [1, 2, 3]
new_list = [40, 50, 60]
for i in zip(mylist, new_list):
    print (i)

# 실행 결과
# (1, 40)
# (2, 50)
# (3, 60)



Example #2 - 여러 개의 Iterable 동시에 순회할 때 사용

list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []

for number1, number2, number3 in zip(list1, list2, list3):
    print(number1 + number2 + number3)

# 실행 결과
# 493
# 124
# 66
# 305



Example #3 - Key 리스트와 Value 리스트로 딕셔너리 생성하기
-> 파이썬의 zip 함수와 dict 생성자를 이용하면 코드 단 한 줄로, 두 리스트를 합쳐 딕셔너리로 만들 수 있습니다.

    animals = ['cat', 'dog', 'lion']
    sounds = ['meow', 'woof', 'roar']
    answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
'''
