#accessing nested dictionary using for loop
a = {1:{'course': 'python', 'fees': 1500},
     2:{'course': 'javascript', 'fees':10000}}

print("ID:")
for id in a:
    print(id)
print()   

# keys 
print("keys:")
for id in a:
    for k in a[id]:
        print(k,'=',a[d][k])
print()    
 