data=[]
with open('hostlist.txt', 'r') as f:
    dat=f.readlines()
b=''
for i in dat:
    a=(i.rstrip("\n"))
    print('"{}",'.format(a))