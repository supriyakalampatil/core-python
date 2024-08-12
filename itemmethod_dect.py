#Dictionary - items() method
stu ={101: 'supriya', 102:'aastha', 103:'asavali'}
print("original dict:")
print(stu)
print()


it = stu.items()
print(it)
print(type(it))
print()

lst =list(it)
print(lst)
print(type(lst))
print()


for r in lst:
    for c in r:
        print(c)
        