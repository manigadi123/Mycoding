l=[10,4,3,54,67,43,86]
m=[]
for i in range(len(l)):
    for j in range(i,len(l)+1):
        m.append(sum[i:j])
print max(m)
