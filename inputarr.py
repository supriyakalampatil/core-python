from numpy import *
m = int(input("Enter number of rows:"))
n = int(input("Enter number of columns:"))
a = zeros((m, n),dtype=int)
u = len(a)
print(a)
for i in range(u):
    for j in range(len(a[i])):
        x = int(input("enter element:"))
        a[i][j]=x
        
for i in range(u):
    for j in range(len(a[i])):
        print(a[i][j])
print(a)        
        
      