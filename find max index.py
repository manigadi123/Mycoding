l=[10,20,39,0.30,-20,-19,45]
for i in range(len(l)):
    if sum(l[:i])==sum(l[i:]):
        print i-1
