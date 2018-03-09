from io import BytesIO
from flask import Flask, render_template, send_file, make_response
import flask
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import matplotlib.pyplot as plt
 
app = flask.Flask(__name__)
 
# mypic 을 호출하면 mypic.html 로 렌더링 합니다.
@app.route('/mypic')
def mypic():
    return flask.render_template("mypic.html")
 
# matplotlib 그래프 파일을 생성하여 MIME 형식으로 보내줍니다. 
@app.route('/plot')
def plot():
 
   # 그림판을 준비합니다.
    fig, axis = plt.subplots(1)
    
   # 데이터를 준비합니다.
    y = [1,2,3,4,5]
    x = [0,2,1,3,4]
 
    # 데이터를 캔버스에 그립니다.
    axis.plot(x,y)
    canvas = FigureCanvas(fig)
    
    # 그려진 img 파일 내용을 html 랜더링 쪽에 전송합니다.
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')
 
 
if __name__ == '__main__':
    port = 5000
    app.debug = True
    app.run(port=port)
