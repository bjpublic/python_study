import plotly.graph_objs as go
import numpy as np
import plotly.offline as offline
 
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
offline.plot(data, filename='basic-scatter.html')