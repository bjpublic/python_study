import numpy as np
import matplotlib.pyplot as plt
 
# x, y 좌표 지정(y = 3x + 1), 방정식 모델을 지정합니다.
x = np.array([1, 2, 5, 7])
y = np.array([4, 7, 16, 22])
A = np.vstack([x, np.ones(len(x))]).T
 
# 선형대수 라이브러리의 least squre 호출합니다.
slope, intercept = np.linalg.lstsq(A, y)[0]
print("기울기:", slope, ", 절편:", intercept)
 
# 기존 값을 점으로, 찾은 기울기를 선으로 그립니다..
plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, slope*x + intercept, 'r', label='Fitted line')
plt.legend()
plt.show()
