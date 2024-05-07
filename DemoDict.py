# DemoDict.py

colors = {"apple" : "red", "banana" : "yellow"}
print(colors)
print(type(colors))
print(len(colors))

#추가
colors["kiwi"] = "green"

#삭제
del colors["apple"]
print(colors)

for item in colors.items():
    print("fruits : %s, color : %s" % item)

for k,v in colors.items():
    print("fruits : %s, color : %s" % (k, v))

# Call by Reference : 파이썬은 항상 참조
x = [5, 6]
y = x
print(x)
print(y)
x.append(7) #x 만 수정

# y도 같이 수정됨
print(x)
print(y)