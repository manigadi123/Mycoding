
def removeDup(l):
    l=[]
    s=set()
    for i in l:
        if i not in s:
            s.add(i)
            l.append(i)
    return l
l=[1,2,3,22,2,2,3,3,4,4,5,6,7,5]
print removeDup(l)
