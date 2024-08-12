def decor(fun):
    def inner():
        print("if: before enhancing function")
        fun()
        print("if:after enhancing function")
    return inner    

def num():
    print("we will use this function")
    print("and will enhance this in decorator")

result_fun = decor(num)     
result_fun()