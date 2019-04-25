def merge(l,m):
    p=[(l[i],m[i]) for i in range(0,len(l))]
    return p
l=[1,2,3,4,5]
m=[5,6,7,8,9]
print merge(l,m)
