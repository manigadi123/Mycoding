l=[-5,40,-30,20,10,-5]
d={}
for i in range(len(l)):
    for j in range(i,len(l)):
        d[sum(l[i:j])]=l[i:j]
print d[max(d.keys())]
