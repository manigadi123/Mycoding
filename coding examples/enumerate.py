l=[12,24,35,70,88,120,155]
m=[x for (i,x) in enumerate(l) if i%2!=0]
print m

o=[x for (i,x) in enumerate(l) if i not in (0,4,5)]
print o
