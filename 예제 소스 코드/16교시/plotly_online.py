import plotly 
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

# API 키 정보를 넣습니다.
plotly.tools.set_credentials_file(username='사용자 이름', api_key='사용자의 API KEY')

# 랜덤 값을 만듭니다.
N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# 트레이스를 만듭니다.
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

data = [trace]

# 그래프를 그립니다.
py.plot(data, filename='basic-scatter')