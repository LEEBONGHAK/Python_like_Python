'''
정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어짐
solution 함수가 mylist 각 원소의 길이를 담은 리스트를 return

Ex)
input	                output
[[1], [2]]	            [1, 1]
[[1, 2], [3, 4], [5]]	[2, 2, 1]
'''


def solution(mylist):
    answer = list(map(len, mylist))
    return answer


input1 = [[1], [2]]
print(input1)
print(solution(input1))
print("\n")


input2 = [[1, 2], [3, 4], [5]]
print(input2)
print(solution(input2))
