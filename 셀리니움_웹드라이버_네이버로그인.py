# 셀리니움_웹드라이버_네이버로그인.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import clipboard
import time

#selenium 4.6이상은 웹드라이버 설치 없이 사용 
driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login')

# 아이디 : <input type="text" id="id" name="id" placeholder="아이디" title="아이디" class="input_text" maxlength="41" value="">
# 패스워드 : <input type="password" id="pw" name="pw" placeholder="비밀번호" title="비밀번호" class="input_text" maxlength="16">
# 로그인 버튼 : <button type="submit" class="btn_login" id="log.login">
#               <span class="btn_text">로그인</span>
#              </button>

# 로그인 창에 아이디/비밀번호 입력
loginID = "ID"
clipboard.copy(loginID)                 #ID를 클립보드에 복사 후 
#mac은 COMMAND, window는 CONTROL
driver.find_element(By.XPATH,'//*[@id="id"]').send_keys(Keys.CONTROL, 'v')  # Ctrl + v로 클립보드에 복사한 ID 입력

loginPW = "PASSWORD"
clipboard.copy(loginPW)                 #PW를 클립보드에 복사 후
driver.find_element(By.XPATH,'//*[@id="pw"]').send_keys(Keys.CONTROL, 'v')  # Ctrl + v로 클립보드에 복사한 PW 입력
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="log.login"]').click()

while True:
    pass 