l=[[1,2,-1],[1,2,3],[3,21,1],[-1,-2,-3]]
def foo(m):
    return m[-1]
print sorted(l,key=foo)

