# 모듈을 불러옵니다.
import cx_Oracle

# 데이터베이스에 연결합니다.
dsnStr = cx_Oracle.makedsn("127.0.0.1", "1521", "xe")
con = cx_Oracle.connect(user="pyuser", password="test1234", dsn=dsnStr)

# 커서를 만듭니다.
cur = con.cursor()

# 커서에 쿼리를 입력해 실행 시킵니다
cur.execute('select * from supermarket')

# 데이타를 모두 가져옵니다.
res = cur.fetchall()

# 가져온 내용을 한 줄씩 가져와서, 각 컬럼의 내용을 공백으로 구분해 출력합니다. 
for row in res:
    print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " "  + str(row[3]) + " " + str(row[4]))             

# 연결을 닫습니다.
cur.close()
con.close()