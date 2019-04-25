l=[1,2,3,4,5,6,7,8,8,10]
e=filter(lambda x:x%2==0,l)
print e
f=[i for i in l if i%2==0]
print f

g=[i for i in l if i%2!=0]
print g
