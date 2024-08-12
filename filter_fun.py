a =[10,50,60,80,5,45,65]

def high_marks(n):
    if n>=60:
        return True
    
result = list(filter(high_marks, a))
print(result)
print(type(result))  
for i in result:
    print(i)

