

x =[55,89,5,45,98,12,6,34,86.34]
print("Original list")
n = len(x)
for i in range(n):
     print(i,"=", x[i])
print()
print("from 0th position to 5th position stride 2")
e = x[1:6:2]
for i in e:
    print(i)
print()        


