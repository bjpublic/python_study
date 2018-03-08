from sympy import *
 
# x 를 심볼로 지정합니다.
x = symbols('x')
 
# y = x^2 - x - 6 의 인수분해를 합니다.
ans = factor(x**2 - x - 6)
print(ans)
