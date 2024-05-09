# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):          # 객체를 string으로 설정
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
# account1.balance = 150_000_000  # 외부에서 수정 가능... BUG

print(account1)                 #__str__ 정의가 되어있어 print 가능

# 테스트
# account1.__balance = 150_000_000    # 접근 불가 (Error는 발생 안함..??) - account1의 __balance의 값이 변경된 것이 아닌 account1에 __balance라는 멤버변수가 별도로 생성됨..
# account1.balance = 100_000_000
# print(account1.__balance)           # 위 코드처럼 호출이 되면 해당 부분 error 발생 안함 BUG
# print(account1.balance)

# print(account1)