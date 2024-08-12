#get() method 
#this method returns the value of the specifide key.
#if key is not found then it will return none or default value.
#sysntax:- dict.get(key,defaultvalue)
stu = {101: 'rahul', 102:'raj', 103: 'soham'}
print("original doct:")
print(stu)
print()

print(stu.get(104,"hello hi key avalable nahi"))
