# DemoOSPath.py

import os
import os.path
import random

# random
print(random.random())
print(random.random())

# 중복 숫자 가능
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print()

# 중복 없이 샘플링 (로또번호)
for i in range(5):
    print(random.sample(range(1,46), 6))

fileName = r"c:\python310\python.exe"   #r을 사용하면 \를 두 번 쓸 필요 없음
print(os.path.abspath("python.exe"))
print(os.path.basename(fileName))

if os.path.exists(fileName):
    print("파일 크기 : ", os.path.getsize(fileName), "byte")
else:
    print("파일 없음!")


import glob
#print(glob.glob(r"c:\work\*.py"))
for item in glob.glob(r"c:\work\*.py"):
    print(item)