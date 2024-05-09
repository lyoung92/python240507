# 전역변수
strName = "Not Class Member"

class DemoString:
    def __init__(self):
        self.strName = ""   # 멤버 변수
    def set(self, msg):
        self.strName = msg
    def print(self):
        #print(strName)      # 멤버변수가 아닌 전역변수를 print하고 있음.. BUG!!
        print(self.strName)  # 멤버변수를 print 하도록 수정!!

d = DemoString()
d.set("First Message")
d.print()
