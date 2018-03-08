from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Firefox 웹 드라이버를 생성 합니다. 
driver = webdriver.Firefox()

# 구글 페이지를 호출해 가져옵니다.
driver.get("https://www.google.com")
