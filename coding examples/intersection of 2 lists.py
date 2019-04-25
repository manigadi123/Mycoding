def removeDuplicate(l):
    m=[]
    p=set()
    for i in l:
        if i not in p:
            p.add(i)
            m.append(i)
    return m
l=[1,3,4,6,8,4,8,9]
print removeDuplicate(l)
