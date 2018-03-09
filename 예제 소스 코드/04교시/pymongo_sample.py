# 모듈을 불러옵니다.
import json
import pymongo
from pymongo import MongoClient

# 데이터베이스에 연결합니다.
client = MongoClient("localhost", 27017, maxPoolSize=50)

# supermarket 컬렉션을 찾습니다.
db=client.admin
collection=db['supermarket']
cursor = collection.find({},{'_id': False})

# 커서를 루프로 돌립니다(i 에는 0 부터 루프의 숫자가 들어갑니다).
for i, document in enumerate(cursor):
    rowcontent = ""
    keycontent = ""
    
    # 다큐먼트에서 키와 값을 가져와서 공백으로 구분해 문자열로 만듭니다.
    for key, val in document.items():
        keycontent = keycontent + "   " + str(key)
        rowcontent = rowcontent + "   " + str(val)
    
    # 만약 첫 번째 루프라면 키 이름도 출력해 칼럼 이름 출력하는 것을 흉내냅니다.
    if i == 0:
        print(keycontent)
        print (rowcontent)
    else:
        print (rowcontent)
    i += 1