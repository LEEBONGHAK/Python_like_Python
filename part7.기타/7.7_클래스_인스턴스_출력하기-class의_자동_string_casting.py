'''
클래스 인스턴스 출력하기 - class의 자동 string casting
- 인스턴스 출력 형식을 지정하는 방법

예) 2차원 평면 위의 점을 나타내는 Coord 클래스의 
    인스턴스를 (x 값, y 값)으로 출력하기
'''

# 일반적인 방법 - 1


class Coord(object):
    def __init__(self, x, y):
        self.x, self.y = x, y


point = Coord(1, 2)
print(f"({point.x}, {point.y})")


# 일반적인 방법 - 2
def print_coord(coord):
    print(f"({coord.x}, {coord.y})")


print_coord(point)
print('\n')



# in Python
# __str__ 메소드 사용하여 class 내부에서 출력 format 지정 가능
class Coord_Python(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"


point_2 = Coord_Python(1, 2)
print(point_2)
