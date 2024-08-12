#nested function
"""
def disp():
    def show():
        print("show function ")
    print("Didsp function")
    show()

disp()    
"""

def disp():
    def show():
        return "show function"
    result =show()+ " disp function"
    return result

a = disp() 
print(a)











