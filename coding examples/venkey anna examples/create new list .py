l=[1,2,3,'m','n','o',1,2,3,4,5,6,6,6,7,1,2,3,4]
m=[]
for i in l:
    if i not in m:
        m.append(i)
print m

s="mani is a good boy"
d={}
for i in s:
    if d.has_key(i):
        d[i]=d[i]+1
    else:
        d[i]=1
print d

d1={}
for i in s:
    d1[i]=d.get(i,0)+1
print d1

