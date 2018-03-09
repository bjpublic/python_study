from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
# Firefox 웹 드라이버를 생성 합니다. 
driver = webdriver.Firefox()
 
# 구글 페이지에서 "파이썬 공부" 라고 검색해 옵니다.
driver.get("https://www.google.com/search?q=파이썬 공부")
 
# 검색 된 div 태그 안에 들은 링크 들을 가져옵니다.
results = driver.find_elements_by_css_selector('div.g')
 
# 그 중 첫번째 링크 안에서 a 태그를 찾습니다.
link = results[0].find_element_by_tag_name("a")
 
# a 태그 안에서 href 이라는 속성을 가져옵니다.
href = link.get_attribute("href")
 
# 속성 안에서 q 에 해당되는 값을 가져옵니다.
import urlparse
print(urlparse.parse_qs(urlparse.urlparse(href).query)["url"])
