from numpy import *
n =int(input("Enter Number of elements:")) #get input number of element
a =zeros(n,dtype=int)

for i in range(len(a)):
    x=int(input("enter element:"))
    a[i]=x
    
    for i in range(len(a)):
        print(a[i])