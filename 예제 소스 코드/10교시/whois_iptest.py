import json
import requests  
 
# 요청 세션을 하나 만듭니다.
s = requests.session()
 
# API 를 호출합니다.
con = s.get('http://whois.kisa.or.kr/openapi/whois.jsp?query=202.30.50.51&key=발급받은키&answer=json')
 
# 호출 받은 API 결과를 json 형태로 받습니다.
json_data = json.loads(con.text)
 
# 결과를 저장할 빈 리스트 생성합니다.
WhoIsData = []
 
# 피들러에서 파악했던 값들을 하나씩 추출해 리스트에 담습니다.
WhoIsData.append(json_data['whois']['query'])
WhoIsData.append(json_data['whois']['countryCode'])
WhoIsData.append(json_data['whois']['korean']['PI']['netinfo']['addr'])
WhoIsData.append(json_data['whois']['korean']['PI']['netinfo']['range'])
WhoIsData.append(json_data['whois']['korean']['PI']['netinfo']['servName'])
 
# 리스트를 출력 합니다.
print(WhoIsData)
