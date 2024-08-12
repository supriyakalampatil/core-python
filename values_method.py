#dictionary - values() method
stu ={101: 'rahul', 102:'priya', 103:'manasi'}
print("original dict:")
print(stu)
print()

all_value =stu.values()
print(all_value)
print(type(all_value))
print()

values_lst= list(all_value)
print(values_lst)
print(type(values_lst))
print()

for v in values_lst:
    print(v)
