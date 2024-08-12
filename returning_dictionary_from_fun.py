#passing and returning Dictionary 
def show(d):
    print(d)
    print(type(d))
    for k in d:
        print(k,'=',d[k])
    return d

dc = {101:'rama', 102:'raj', 103:'gauri'}
new_dc =show(dc)
print(new_dc)
print(type(new_dc))
    