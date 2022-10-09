data=[]
import math
import sys
file_name=sys.argv[2]
with open('hostlist.txt', 'r') as f:
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
# 800
#     8 groups of 100
#  1*100 = 0:100
#  2*100 = 100:200
#  3*100 = 200:300
#  4*100 = 300:400
#  5*100 = 400:500
#  6*100 = 500:600
#  7*100 = 600:700
#  8*100 = 700:800
