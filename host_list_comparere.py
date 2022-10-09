import sys
host_list_1= (sys.argv[1])
host_list_2= sys.argv[2]



data=[]
with open(sys.argv[1], 'r') as f:
    dat=f.readlines()
h_1_data=[]


for i in dat:
    a=(i.rstrip("\n"))
    h_1_data.append('{}'.format(a))



h_2_data=[]
data=[]

with open(sys.argv[2], 'r') as f:
    dat=f.readlines()

for i in dat:
    a=(i.rstrip("\n"))
    h_2_data.append('{}'.format(a))
    
for i in h_2_data:
    if i not in h_1_data:
        print(i)