#anonymus function or lambda function
"""
def show(x): #
    print(x) #      this is normal finction
             #
show(5)      #




show =lambda x : print(x)#      this is lambda functiom
show(5)                  #

"""

add_sub  = lambda x, y : (x + y, x -y)
a,s = add_sub(5, 2)
print(a)
print(s)
