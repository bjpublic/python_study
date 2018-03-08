import pandas as pd
import numpy as np
 
# pandas 용 dataframe 을 만듭니다(메모리 버전 엑셀이라고 생각합니다)
df = pd.DataFrame({'A': 'fruit drink cookie fruit'.split(),
                   'B': 'orange Coke chocopie mango'.split(),
                   'C': np.arange(4)})
 
# 만든 dataframe 을 출력합니다.
print(df)
print('------------------------------')
 
# 뿌리면 아래와 같이 생겼습니다.
#      A         B      C
# 0  fruit    orange    0
# 1  drink    juice     1
# 2  cookie   chocopie  2
# 3  fruit     mango    3
 
# df 중에 A 열이 fruit 인 데이터만 추출 하여 출력 합니다.
print(df.loc[df['A'] == 'fruit'])
