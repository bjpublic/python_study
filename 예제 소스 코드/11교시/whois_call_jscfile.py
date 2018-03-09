import requests
import re

# jsc 페이지를 post 로 호출합니다.
payload = {'query': '202.30.50.51', 'ip': '1.225.79.26'}
r = requests.post("https://whois.kisa.or.kr/kor/whois.jsc", data=payload)

# 받아온 페이지의 인코딩을 지정 합니다.
r.encoding = 'utf-8'
# print(r.text) 
 
 
# 정규표현식을 이용해 결과에서 주소를 얻어옵니다.
pattern = re.compile("주소.*: ([^0-9].*)")
match = re.findall(pattern, r.text)
print (match[0]) 
