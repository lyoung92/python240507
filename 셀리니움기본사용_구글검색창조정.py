from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time 

#크롬드라이버 실행
driver = webdriver.Chrome() 
#url주소 추가해서 실행 
driver.get("https://www.google.co.kr")
#창이 오픈되고 3초를 대기한다. 
time.sleep(3)

#<textarea class="gLFyf" aria-controls="Alh6id" aria-owns="Alh6id" autofocus="" title="검색" value="" jsaction="paste:puy29d;" aria-label="검색" aria-autocomplete="both" aria-expanded="false" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" id="APjFqb" maxlength="2048" name="q" role="combobox" rows="1" spellcheck="false" data-ved="0ahUKEwjMxp3Z6_-FAxUiklYBHc3dA8sQ39UDCA4"></textarea>
#검색어창 찾기
searchBox = driver.find_element(By.CLASS_NAME, "gLFyf")
#XPath를 사용하는 경우
#//*[@id="APjFqb"]
#searchBox = driver.find_element(By.XPATH,"//*[@id='APjFqb']")

searchBox.send_keys("맥북")
searchBox.send_keys(Keys.RETURN)
#time.sleep(5)

# 창을 계속 열어 둘 때
while True:
    pass
