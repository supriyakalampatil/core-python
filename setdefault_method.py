#dictionary - setdefault() method
stu ={101: 'supriya', 102: 'bhagyashree',103: 'vijay'}
print("original dict")
print(stu)
print(id(stu))
print()

returned_value =stu.setdefault(109,'python')
print("after setDefault dict:")
print(stu)
print(id(stu))
print("returning value:",returned_value)
print()
