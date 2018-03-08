from selenium import webdriver
 
# Firefox 웹 드라이버를 생성 합니다. 
browser = webdriver.Firefox()
 
# 구글 페이지에서 "파이썬 공부" 라고 검색해 옵니다.
browser.get("https://www.google.com/search?q=파이썬 공부")
 
# 검색 된 div 태그 안에 들은 링크 들을 가져옵니다.
results = browser.find_elements_by_css_selector('div.g')
 
# 인자를 담을 리스트를 만듭니다.
hrefs = []
 
# div 중 최초 5개를 가져와서, 그 안에서 a 태그를 찾고, a 태그 안의 href 속성을 찾습니다. 
for i in range(0, 5):
    link = results[i].find_element_by_tag_name("a")
    hrefs.append(link.get_attribute("href"))
 
# 화면에 출력해 봅니다.
for href in hrefs:
    print(href)
 
# 각 링크에 대해서 새 탭에서 엽니다.
for href in hrefs:
    browser.execute_script('window.open("' + href + '","_blank");')
