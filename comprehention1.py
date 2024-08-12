lst1 =[]
for i in range(20):
    if(i%2==0):
        lst1.append(i)
print(lst1)   
print()

#with list comprehention (conditional)

lst2 = [i for i in range (20) if i%2==0]
print("new List:", lst2)

#with list compfrehention (conditional)
lst2 =[i for i in range(20) if i%2==0]
print("new list:", lst2)

