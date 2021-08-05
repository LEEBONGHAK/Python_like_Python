'''
    solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.

    Ex)
    mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]일 경우 경우, 
    solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 return
'''


def solution(mylist):
    answer = []

    for i in range(len(mylist)):
        temp = []
        for j in range(len(mylist)):
            temp.append(mylist[j][i])
        answer.append(temp)

    return answer


mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(mylist)
print(solution(mylist))
