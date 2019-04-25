d={}
s=raw_input("Enter youur string:")
for i in s:
    d[s]=d.get(s,0)+1
print 'Yn'.join(['%s %s' %(k,v) for k,v in d.items()])
