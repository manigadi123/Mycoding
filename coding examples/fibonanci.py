#if the value of i=4,the out should be dict (i,i*i)

n=int(input())

d=dict()
for i in range (1,n+1):
    d[i]=i*i
print d
