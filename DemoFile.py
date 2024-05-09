#DemoFile.py

#파일쓰기
f = open("demo.txt", "wt", encoding = "utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일 읽기
#read
print("== read ==")
f = open("demo.txt", "rt", encoding = "utf-8")
result = f.read()
print(result)

#readline
print("== readline ==")
f.seek(0)
result = f.readline()
print(result, end = "")       #첫번째
result = f.readline()
print(result, end = "")       #두번째

#readlines
print("== readlines ==")
f.seek(0)
result = f.readlines()
print(result)       #['첫번째\n', '두번째\n', '세번째\n'] : 리스트로 return

f.close()
