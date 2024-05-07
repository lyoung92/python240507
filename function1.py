# funtion1.py
# 함수 정의
def setValue(newValue) :
    x = newValue
    print(x)

#함수 호출
print(setValue(5))

#스코핑 룰 : LGB (Local, Global, Built-in) 순서대로 이름공간에서 검색

x = 1   #전역변수 (Global)
def func(a) :
    return a+x  # x는 Global
def func2(a):
    x = 2
    return a+x # x는 Local (Global이 있으나 LGB 순서로 인해 Local)

a = func(1)
b = func2(1)

print(a,b)

#함수의 인자 : 기본값을 전달하는 경우
def times(a = 10, b = 20) :
    return a*b

print(times())      #a = 10 / b = 20 : 200
print(times(5))     #a = 5 / b = 20 : 100
print(times(5,6))   #a = 5 / b = 6 : 30

#키워드 인자 : 인자 이름으로 값을 전달하는 경우에는 순서를 맞추지 않아도 인자 이름을 지정해서 전달 가능
def connectURI(server, port) :
    strURL = "http://" + server + ":" + port
    return strURL

print(connectURI("naver.com", "80"))    
print(connectURI(port = "8080", server = "daum.net"))   # 순서 변경이 되어도 인자 이름으로 값 전달하여 문제 없음