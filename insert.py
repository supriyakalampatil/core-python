from array import*
stu_roll =array('i',[101,102,103,104])
n= len(stu_roll)
i =0
while(i<n):
    print(stu_roll[i])
    i+=1

print("array after insert")
stu_roll.insert(1,106)
stu_roll.insert(3,107)
n = len(stu_roll)
i =0
while(i<n):
    print(stu_roll[i])
    i+=1   
    