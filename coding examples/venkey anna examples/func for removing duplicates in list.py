
def list(l):
    m=[]
    for i in l:
        if i not in " ":
            i=int(i)
            i+=10
            m.append(i)
    return m
l=["a","b","c",2,3,4,5]
print list(l)        


            
            
