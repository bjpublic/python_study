import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
 
# NumPy 배열에 데이터를 지정합니다.
x = np.array([1, 2, 5, 7])
y = np.array([4, 7, 16, 22])
 
# 데이터에 맞는 값을 찾습니다(Slope: 기울기, Intercept: 절편).
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print ("기울기와 절편", slope, intercept)
print ("R-squared", r_value**2)
 
# 데이터를 점으로, 찾은 선과 같이 화면에 표시합니다.
plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope*x, 'r', label='fitted line')
plt.legend()
plt.show()
