import matplotlib.pyplot as plt
import numpy as np

# 점을 찍을 좌표 대한 리스트를 생성합니다.
x = [1, 2, -3, -4]
y = [1, -2, 3, -4]

# 각각의 색이 담긴 리스트를 돌리면서, 각각의 점에 대해서 색을 지정합니다.
for i, color in enumerate(['red', 'black', 'blue', 'brown'], start=0):
    plt.plot(x[i], y[i], 'ro', color=color)
 
# 그래프의 제목을 넣습니다.
plt.title('Simple Graph')

# 그리드를 보이게 합니다.
plt.grid(True)

# 가로세로 1:1 비율을 만듭니다.
plt.axes().set_aspect('equal', 'datalim')

# x,y 축 이름을 넣습니다.
plt.ylabel('X Axis')
plt.xlabel('Y Axis')

# 그래프가 보이는 최대 최소 범위를 지정 합니다.
plt.xlim((-8,8))
plt.ylim((-8,8))

# x, y 축을 보이게 합니다.
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
 
# 그린 그래프를 화면에 출력 합니다.
plt.show()