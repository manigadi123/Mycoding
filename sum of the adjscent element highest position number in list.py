l=[10,20,30,0.20,50,-599]

m=[]
for i in range(len(l)):
    for j in range(i,len(l)+1):
        m.append(sum(l[i:j]))
print max(m)
