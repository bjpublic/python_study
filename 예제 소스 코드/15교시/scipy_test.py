from scipy.integrate import quad
 
 
# y=x^2 함수를 정의 합니다.
def myfn(x):
    return x**2
 
 
# x 는 0~1 사이의 구간에 대해서 해당 함수를 적분 합니다.
ans, err = quad(myfn, 0, 1)
print (ans)