d={"a":1,'b':2,'c':3}
d1=d
d2=d.copy()
print d1
print d2
print d1 is d2
print d is d1
print d is d2

print d1==d2
print d==d1
print d==d2
print id(d1)
print id(d2)


d['d']=200
print d
print d1
d1['f']=210
print d1
print d
#print d2
print id(d)
print id(d1)



#d2['e']=300
#print d2
#print d
#print id(d2)
#print id(d)
