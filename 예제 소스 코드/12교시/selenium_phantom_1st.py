from selenium import webdriver
 
# firefox 웹 드라이버를 로드 합니다.
browser = webdriver.PhantomJS()
 
# 구글에 "파이썬 공부" 검색어로 조회 합니다.
browser.get("https://www.google.com/search?q=파이썬 공부")
 
# 결과 div 태그를 클래스 기준으로 검색해 다 가져옵니다.
results = browser.find_elements_by_css_selector('div.g')
 
# 인자를 담을 리스트를 만듭니다.
hrefs = []
 
# div 중 최초 5개를 가져와서, 그 안에서 a 태그를 찾고, a 태그 안의 href 속성을 찾습니다. 
for i in range(0, 5):
    link = results[i].find_element_by_tag_name("a")
    hrefs.append(link.get_attribute("href"))
 
# 화면에 결과들을 출력 해봅니다.
for href in hrefs:
    print(href)
