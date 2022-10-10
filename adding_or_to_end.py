data=[]
import math
import sys
file_name=sys.argv[2]
with open(file_name, 'r') as f:
    dat=f.readlines()
limit=100
len_of_file=len(dat)
if len_of_file >limit:

    num=math.ceil(len_of_file/limit)
    print("number is ",num)
    prev=0
    cur=100
    
    for i in range(1,num+1):
        print(i)
        for j in range(prev,cur): #printing 100 times
                a=(dat[j].rstrip("\n"))
                print('{} or '.format(a),end=" ")
                # print(j, "or","",end="")
                
        print("")
        prev=cur
        cur*=i

