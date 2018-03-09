from selenium import webdriver
 
# firefox 웹 드라이버를 로드 합니다.
phantomjs_path = r'c:\Python\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(phantomjs_path)    
 
# 구글에 "파이썬 공부" 검색어로 조회 합니다.
browser.get("https://www.google.com")
input_element = browser.find_element_by_name("q") 
input_element.send_keys("파이썬 공부") 
input_element.submit() 

# 잠시 로딩될 시간을 기다립니다.
import time
time.sleep(2)
 
# 결과 div 태그를 클래스 기준으로 검색해 다 가져옵니다.
results = browser.find_elements_by_css_selector('div.g')
 
# 인자를 담을 리스트를 만듭니다.
hrefs = []
 
# 디버그용 스크린 샷을 만듭니다.
# browser.save_screenshot('screen.png')
 
# div 중 최초 5개를 가져와서, 그 안에서 a 태그를 찾고, a 태그 안의 href 속성을 찾습니다.
for i in range(0, 5):
    link = results[i].find_element_by_tag_name("a")
    hrefs.append(link.get_attribute("href"))
 
# href 에서 q 인자를 추출해 옵니다.
from furl import furl
for href in hrefs:
    f = furl(href) 
    print (f.args['q'])
