# DemoStr.py

strA = "python is very powerful"
strB = "파이썬은단순해"

print(len(strA))
print(len(strB))
print(strA.capitalize())    #첫 글자를 대문자로 수정 : Python is very powerful
print(strA.count("P"))
print("MBC2580".isalnum())  #알파벳 및 숫자로만 구성되어 있는지?    True
print("MBC:2580".isalnum()) #알파벳 및 숫자로만 구성되어 있는지?    False
print("2580".isdecimal())   #숫자로만 구성되어 있는지?      True

data = "<<< spam and ham >>>"
result = data.strip("<> ")      # 앞 뒤로 <, >, 공백이 있으면 삭제
print(data)                     # <<< spam and ham >>>
print(result)                   # spam and ham

result2 = result.replace("spam", "spam egg")
print(result2)

print("== 리스트 변환 ==")
lst = result2.split()   # list로 변환 ['spam', 'egg', 'and', 'ham']
print(lst)              
print(":)".join(lst))   # list를 구분자로 합치기

#정규표현식
import re

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

result = re.search("\d{4}", "올해는 2024년입니다.")
print(result.group())

result = re.search("\d{5}", "우리 동네는 52111")
print(result.group())

result = re.search("apple", "this is apple")
print(result.group())
