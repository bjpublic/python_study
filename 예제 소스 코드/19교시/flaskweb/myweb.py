from flask import Flask
from flask import render_template
import pyodbc

server = 'localhost'
database = 'mytest'
username = 'pyuser'
password = 'test1234'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
 
# flask 웹서버를 실행 합니다.
app = Flask(__name__)
 
# "sqltable" 이라는 URL 인자를 "showsql" 이라는 함수로 연결합니다.
@app.route("/sqltable")
def showsql():
    # SQL 문을 실행하여 supermarket 테이블에서 데이터를 가져옵니다.
    cursor.execute('SELECT Itemno, Category, FoodName, Company, Price FROM supermarket(nolock);')
    # 가져온 모든 데이터를 mytable.html 파일과 함께 랜더링 하여 표현합니다.
    return render_template('myweb.html', rows = cursor.fetchall())
 
# 이 웹서버는 127.0.0.1 주소를 가지면 포트 5000번에 동작하며, 에러를 자세히 표시합니다 
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=True)
