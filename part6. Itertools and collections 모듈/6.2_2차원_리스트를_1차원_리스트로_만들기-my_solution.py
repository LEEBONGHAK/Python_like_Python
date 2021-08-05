'''
문자열을 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어짐
solution 함수가 mylist를 일차원 리스트로 만들어 return

input	                            output
[[1], [2]]	                        [1, 2]
[['A', 'B'], ['X', 'Y'], ['1']]	    ['A', 'B', 'X' ,'Y', '1']
'''


def solution(mylist):
    answer = []
    for i in mylist:
        answer += i
    return answer


my_list = [[1, 2], [3, 4], [5, 6]]
print(my_list)

print(solution(my_list))
