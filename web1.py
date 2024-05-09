# web1.py
# 웹 크롤링을 위한 선언
from bs4 import BeautifulSoup

# 페이지 로딩 : method 체인
page = open("Chap09_test.html", "rt", encoding = "utf-8").read()

# 검색이 용이한 soup 객체 생성(html, xml)
soup = BeautifulSoup(page, "html.parser")

#html 전체 검색
#print(soup.prettify()) 

#<p> 전체 검색
#print(soup.find_all("p"))
# for item in soup.find_all("p"):
#     print(item)

#<p>태그 하나 검색
#print(soup.find("p"))

#필터링 : <p class = 'outer-text'>
#print(soup.find_all("p", class_ = "outer-text"))

#attrs는 속성을 지정
#print(soup.find_all("p", attrs = {"class" : "outer-text"}))

#<p> 태그의 id로 추출
#print(soup.find_all("p", id = "first"))

#내부의 컨텐츠 추출 : .text 속성
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "") # 엔터 삭제
    print(title)