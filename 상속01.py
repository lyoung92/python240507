# 부모클래스 정의
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name
        # self.phoneNumber = phoneNumber
        Person.__init__(self, name, phoneNumber)    #부모 초기화 Method 호출
        self.subject = subject
        self.studentID = studentID
    
    # printInfo 재정의
    def printInfo(self):
        Person.printInfo(self)
        #print("Info(Name:{0}, Phone Number: {1}, subject: {2}, studentID: {3})".format(self.name, self.phoneNumber, self.subject, self.studentID))
        print("Info(subject:{0}, Student ID: {1})".format(self.subject, self.studentID))
    



p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
print(p.__dict__)
print(s.__dict__)

p.printInfo()
s.printInfo()
