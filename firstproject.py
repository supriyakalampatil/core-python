#print("Hello world")

#python variables
"""
name ="supriya"
age= 22
print(name)
print(age)
"""
#Q.add a ersom with name tony stark
#tony's age is 51 years old
#tony is a genius
"""
name ="tony stark"
age =51
print("tony is genius")
print(name)
"""

#get input from user
"""
name = input("what is your name??")
print(" hello " + name)
"""

#type conversion
"""
old_age =input(" enter your old age: ")
new_age =old_age + 2
print(new_age)
nember = 18

print(float(18))
 """

#adding 2 numbers
"""

first = input("enter firt number:")
second = input("enter second number:")

sum = int(first) + int(second) 
print("the sum is :" + str(sum))

"""

#strings
"""
name ="Tony stark"

print(name.upper())
print(name)
print(name.find('stark'))

print(name.replace("stark", "Ironman"))
print(name)

"""
#in keywords 
"""
name ="Tony Stark"
print('T' in name)
"""

#operatiors in python
'''
print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 % 2) #modulo
print(5 // 2)
print(5 ** 2)
'''
"""
i =5
i =i +2
i +=2
i -= 2
i *=2
"""

#operator precidant
"""
result = 2 + 3 / 5
print(result)
"""

#comments
# this is single line comment

"""
this is 
multi line 
commnet """

#comparision operator(it returnboolian value in the form of true and fals)
"""
print(3 <=2)
print(3==3)
print(3 !=3)

"""

#logical operator
"""print(2 > 3 or 2 > 1) 
print(3 > 2 and 2 > 6)
print(not 2 > 3)
"""
#if else statements in python programming
"""
age = 19

if age >= 18:
    print("you are an adult")
    print("you can vote")
elif age < 18 and age > 3:
    print("you are in school")
else:
    print("you are a child")
"""

#create a mini project(calculator)
#let's build a calculator
"""
first = input("enter first number :")
operator = input("enter operator(+,-,*,/,%):")
second = input("enter second number :")

first = int(first)


if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second )
elif operator == "/":
    print(first / second )
elif operator == "%":
    print(first % second)  
else:
    print("invlid operation")

"""

#rage 
"""
numbers = range(5)
print(numbers)
"""

#loops i python 
#(while loop ----jab tak)
"""
i = 1

while i <= 50:
    print(i)
    i = i + 1
"""
""" for * 
i = 5
while i >= 0:

    print(i * "*")
    i = i - 1   
"""       

#range 
"""
for item in range(5):
    print(item + 1)
"""

#list in python
 #list is collection of items
"""
marks = [95, 98, 97]
print(marks[0:2])
"""

"""--------- second example---------- 

marks =[95 , 98, 97]

for score in marks:
    print(score)

"""   
#append operation in python( append is used to add element in list (append adds element at the end of list))

"""
marks = [95, 98 ,97]
marks.append(99)

print(marks)
"""

#insert in python (inser ised when you wand to add or insert element in list at any position )
"""
marks = [95, 98 , 97]

marks.insert(0,99)
print(marks)
"""
#-----> in keyword <---we can check that item is exist in lost or not with help of (in keyword)
"""
marks = [95, 98 , 97]

marks.insert(0, 99)
print(99 in marks)

"""
#we can find length of list how many elements in this list
"""
marks = [95, 98, 97]
marks.insert(0,99)
print(marks)
print(len(marks))
"""
 # by using while loop
"""
marks= [95 , 98, 97]

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1 
"""

#break & continue keywords

#break 
"""
students =["ram", "shyam","krishna","radha","radhika"]

for student in students:
    if student == "radha":
        break;
    print(student)
"""    

#continue
"""
students =["ram", "shyam","krishna","radha","radhika"]

for student in students:
    if student == "krishna":
        continue;
    print(student)
"""

#tuple 
#tuple is like list but only differance is that tuple is imutable(we can not change )
#we can not add,delete,modify anythng


#count will count the number of repetations
"""
marks =(95, 98, 97,97)

print(marks.count(97))
"""
#index
"""
marks =(95, 98, 97, 97)

print(marks.index(97))
"""
#set is used for store unique data not duplicate
"""
marks ={95, 98, 97, 97,97}
#[], (), {}

person = "ram", "sham","abhi"

print(person)
"""
#sets are unorderd  it has no index
"""
marks = {95, 98, 97, 97, 97}

for score in marks:
    print(score)
"""

#dictionary in python
#it contents key and value pair
"""
marks = {"english" : 95, "chemestry" : 98}
information = {"ram": "balkishna"}

print(marks)
"""

#if we want to access infromation then
"""
marks = {"english" : 95, "chemestry" : 98}

print(marks["chemestry"]) 
marks["chemestry"]=97;
print(marks)


marks["english"] =99;
print(marks)
"""


#functons in python
#1. in-built function---->int,bool,char,str etc
#2.module functions---->
#3. user-defined function

 






































