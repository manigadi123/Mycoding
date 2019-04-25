import operator

x={'a':200,'b':32,'d':71,'ww':23}
print sorted(x.items(),key=lambda x:x[1])

print sorted(x.items(),key=operator.itemgetter(1))
