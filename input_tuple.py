#getting input from users - tuple

a =[]
n =int(input("Enter number of elements:"))

for i in range(n):
    a.append(int(input("enter element:")))

print(type(a))    

a = tuple(a)

print(type(a))
print("tuple:")
for element in a:
    print(element)
