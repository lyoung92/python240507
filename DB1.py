#DB1.py

import sqlite3

# 임시로 메모리에 작업
conn = sqlite3.connect(":memory:")

# 실제 구문 실행 cursor 선언
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS PHONE_BOOK \
            (ID INTEGER PRIMARY KEY AUTOINCREMENT  \
            ,NAME TEXT                             \
            ,PHONE_NUM TEXT);")

#입력
cur.execute("INSERT INTO PHONE_BOOK(NAME, PHONE_NUM) VALUES ('전우치','010-222-1234')   \
                                                         ,  ('이순신','010-123-1234')")

# 입력 파라미터로 처리  
name = input("이름 : ")
phoneNum = input("전화번호 : ")
cur.execute("INSERT INTO PHONE_BOOK(NAME, PHONE_NUM) VALUES (?,?);", (name, phoneNum))

#다중 레코드
dataList = (("AAA","010-1111-2222"),("BBB","010-2222-3333"))
cur.executemany("INSERT INTO PHONE_BOOK(NAME, PHONE_NUM) VALUES (?,?);", dataList)

#검색
cur.execute("SELECT * FROM PHONE_BOOK")
for row in cur:
    print(row)  #TUPLE 형식으로 출력


