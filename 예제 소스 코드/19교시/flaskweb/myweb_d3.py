import json
import flask
import numpy as np
 
app = flask.Flask(__name__)
 
# d3sample 을 호출했을때의 템플릿을 설정합니다.
@app.route("/d3sample")
def showsample():
    return flask.render_template("d3sample.html")
 
# D3에서 가져갈 data url을 호출하면 반환할 json 데이터 만들어 냅니다.
@app.route("/data")
def data():
    # 그래프를 그릴 데이터를 지정 합니다.    
    x = ['2017-07-10', '2017-07-11', '2017-07-12', '2017-07-13', '2017-07-14']
    y = [58.13, 53.98, 67.00, 89.70, 99.00]
 
    # 리스트를 json 데이터로 변환 합니다.
    return json.dumps([{"date": x[i], "close": y[i]}
        for i in range(5)])
 
# 앞과 비슷한데 문법만 조금 틀립니다.
if __name__ == "__main__":
    port = 5000
    app.debug = True
    app.run(port=port)
