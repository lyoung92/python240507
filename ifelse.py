# ifelse.py
# 분기 반복 구문

# score = int(input("점수를 입력 : "))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score :
#     grade = "B"
# elif 70 <= score :
#     grade = "C"
# else : 
#     grade = "D"

# print("등급은 : ", grade)

# value = 5

# while value > 0 :
#     print(value)
#     value -= 1

# lst = [100, "apple", 3.14]
# for item in lst :
#     print (item)

# fruits = {"apple":100, "kiwi":200}
# for k,v in fruits.items():
#     print(k,v)

# print("---range()함수---")
# print(list(range(2000,2025)))   # 2000년 ~ 2024년
# print(list(range(1,32)))        # 1일 ~ 31일

# 리스트 함축(리스트 컴프리헨션)
print("---리스트 함축(리스트 컴프리헨션)---")
lst = list(range(1,11))
print(lst)
print([i**2 for i in lst if i > 5]) # [가공식 for 변수 in 리스트명 if 조건문]
d = {100:"apple", 200:"kiwi"}
print([v.upper() for v in d.values()])

# 필터링
print("---필터링---")
lst = [10,20,30]
iterL = filter(None, lst)   # None : 필터링 없음
for item in iterL:
    print(item)

# 함수 정의
def getBiggerThan20(i):
    return i > 20

print("---20보다 큰 숫자로 필터링---")
iterL = filter(getBiggerThan20, lst) # 사용자 정의 함수로 필터링 
for item in iterL:
    print(item)

print("---람다함수 사용한 필터링---")
iterL = filter(lambda x : x > 20, lst) # lambda 함수로 필터링
for item in iterL:
    print(item)