# DemoListTuple.py

lst = [1,2,3]
print(len(lst))
lst.append(4)
print(lst)
lst.remove(2) #인덱스가 아닌 내부 객체를 지우는 것
# lst.remove(0) -> 오류
print(lst)

print("---Tuple형식---")
tp = (10,20,30)
print(len(tp))

print("---Set형식---")
a = {1,2,3,3}
b = {3,4,5,4}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("---Tuple 형식 사용---")
def calc(a,b):
    return a+b, a*b
#호출
result = calc(3,4)
print(result)
#print(type(result))

print("id : %s, name : %s" % ("Lee","이건녕"))

args = (5,6)
print(calc(*args))  # 매개변수에 *붙으면 tuple

print("--- 형식 변환 ---")
tp = (10,20,30)
a = list(tp)
a.append(40)
print(type(a))
print(a)

