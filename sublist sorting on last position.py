l=[[1,2,2],[-2,1],[10,02,5],[12,90,-1]]
def foo(l):
    return l[-1]
print sorted(l,key=foo)
