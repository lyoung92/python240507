# Person.py 
# 클래스 형식 정의
class Person:
    def __init__(self): # 클래스의 Method의 첫번째 파라미터는 항상 자기 자신으로 예약되어있음 (관용적으로 self 명칭 사용)
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

# 인스턴스 생성
p1 = Person()
p2 = Person()

# Method 호출
p1.name = "전우치"
p1.print()
p2.print()
