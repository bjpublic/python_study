# 모듈을 불러옵니다.
import pymssql

# 데이터베이스에 연결합니다.
conn = pymssql.connect(server='localhost', user='pyuser', password='test1234', database='mytest')

# 커서를 만듭니다.
cursor = conn.cursor()

# 커서에 쿼리를 입력해 실행 시킵니다.
cursor.execute('SELECT Itemno, Category, FoodName, Company, Price FROM supermarket(nolock);')

# 한 행을 가져옵니다.
row = cursor.fetchone()

# 행이 존재할 때까지, 하나씩 행을 증가시키면서 1번째 컬럼을 숫자 2째번 컬럼을 문자로 출력합니다.
while row:
    print("ID=%d, Category=%s" % (row[0], row[1]))
    row = cursor.fetchone()

#연결을 닫습니다.
conn.close()