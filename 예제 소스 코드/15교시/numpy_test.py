import numpy as np
 
# 2*2 크기인 array "a" 를 만듭니다.
a = np.array([[1, 2], [3, 4]])
 
# a array 원소들에 모두 1을 더해 array "b" 를 만듭니다
b = a + 1
print (b)
 
# b array 를 재 정렬해 1*4 로 array "c" 를 만듭니다.
c = np.reshape(b, (1,4))
print (c)
 
# c array 원소들에 log 함수를 적용해 array "d" 를 만듭니다. 
d = np.log(c)
print (d)
