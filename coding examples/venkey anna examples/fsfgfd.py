d={1:2,2:3,3:4}
m={}
for k,v in d.items():
    if v in m:
        print v
    else:
        m[v]=k
print m
