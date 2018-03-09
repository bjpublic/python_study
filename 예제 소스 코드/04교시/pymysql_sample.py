# 모듈을 불러옵니다.
import pymysql

# 연결 문자열을 세팅합니다.
server = 'localhost'
user = 'pyuser'
password = 'test1234'
dbname = 'mytest'

# 데이터베이스에 연결합니다.
conn = pymysql.connect(server, user, password, dbname, charset='utf8')

# 커서를 만듭니다.
cursor = conn.cursor()

# 커서에 쿼리를 입력해 실행 시킵니다.
cursor.execute('SELECT * FROM supermarket;')

# 한 행을 가져옵니다.
row = cursor.fetchone()

# 행이 존재할 때까지, 하나씩 행을 증가시키면서 모든 컬럼을 공백으로 구분해 출력합니다.
while row:
    print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " "  + str(row[3]) + " " + str(row[4]))
    row = cursor.fetchone()
    
# 연결을 닫습니다.
conn.close()

 


