#dictionary - keys() method
stu = {101: 'rahul', 102: 'rohini',103:'rajnndini'}
print("original dict:")
print(stu)
print()

all_keys = stu.keys()
print(all_keys)
print(type(all_keys))
print()


keys_lst = list(all_keys)
print(keys_lst)
print(type(keys_lst))
print()

print(keys_lst[0])

for k in keys_lst:
    print(k)
    
