from numpy import *
a =array([100,200,300,400,500])
b =array([100,20,30,400,50])
result= where(a>b, a,b)
print(result)