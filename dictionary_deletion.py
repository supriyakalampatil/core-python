#we can delete item of dectionary or entire dictionary using del statement.
stu={101: 'rahul', 102:'raj', 103:'sonam'}
print("before deletion:")
print(stu)
print(id(stu))
print()


del stu[102]
print("After deletion:")
print(stu)
print(id(stu))
print()  

 