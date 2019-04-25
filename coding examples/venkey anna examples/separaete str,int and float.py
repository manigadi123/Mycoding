ll=[1,2,3,'m','n','o',1.2,1.4,23.0]
ss=""
flt=[]
for i in ll:
    if isinstance(i,int):
        ll.append(i)
    if isinstance(i,str):
        ss +=i
    if isinstance(i,float):
        flt.append(i)
print ll
print ss
print flt
        
