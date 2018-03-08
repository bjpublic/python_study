# 모듈을 불러옵니다.
import sqlite3

# test.db 연결합니다(SQLite 는 없으면 자동으로 생성합니다).
conn = sqlite3.connect("test.db", isolation_level=None)
cursor = conn.cursor()

 
# 테이블이 없다면 해당 테이블을 생성합니다.
cursor.execute("""CREATE TABLE IF NOT EXISTS supermarket(Itemno INTEGER, Category TEXT,
FoodName TEXT, Company TEXT, Price INTEGER)""")

# 테이블의 내용을 모두 지웁니다.
sql = "DELETE FROM supermarket"
cursor.execute(sql)

# 테이터를 2건 입력 합니다.
sql = "INSERT into supermarket(Itemno, Category, FoodName, Company, Price) values (?, ?, ?, ?, ?)"
cursor.execute(sql, (1, '과일', '자몽', '마트', 1500))

sql = "INSERT into supermarket(Itemno, Category, FoodName, Company, Price) values (?, ?, ?, ?, ?)"
cursor.execute(sql, (2, '음료수', '망고주스', '편의점', 1000))

# 입력된 데이터를 조회합니다.
sql = "select Itemno, Category, FoodName, Company, Price from supermarket"
cursor.execute(sql)


# 데이타를 모두 가져옵니다.
rows = cursor.fetchall()

# 가져온 내용을 한 줄씩 가져와서, 각 컬럼의 내용을 공백으로 구분해 출력합니다.
for row in rows:
    print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]))

# 연결을 닫습니다.
conn.close()