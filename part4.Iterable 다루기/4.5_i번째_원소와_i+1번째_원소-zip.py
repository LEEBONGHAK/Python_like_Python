'''
숫자를 담은 리스트 mylist가 solution 함수의 파라미터로 주어질 때,
solution 함수가 mylist의 i번째 원소와 i+1번째 원소의 차를 담은 일차원 리스트에 차례로 담아 return

단, 마지막에 있는 원소는 (마지막+1)번째의 원소와의 차를 구할 수 없으니, 이 값은 구하지 않음

mylist = [83, 48, 13, 4, 71, 11]
output = [35, 35, 9, 67, 60]
'''

# 파이썬의 zip을 이용하면 index를 사용하지 않고 각 원소에 접근 가능

def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]    

    print(mylist)
    print(solution(mylist))

'''
zip 함수 주의 !!!

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. 
The iterator stops when the shortest input iterable is exhausted.
'''