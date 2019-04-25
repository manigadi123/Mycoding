l=[1,2,3,'m','n','o']
str_v=[]
int_v=[]
for i in l:
    if isinstance(i,int):
        int_v.append(i+10)
    elif isinstance(i,str):
        str_v.append(i)
print int_v
print str_v

