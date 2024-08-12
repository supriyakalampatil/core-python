from numpy import *
m = int(input("enter number of rows:"))
n = int(input("enter number of columns:"))
a = zeros((m, n),dtype=int)
print(a)

#this is for lenghth
u =len(a)
i =0
while(i<u):
    j =0
    while j < len(a[i]):
        x = int(input("Entetr element:"))
        a[i][j] =x
        j+=1
    i+=1

i =0
while i<u:
    j=0  


