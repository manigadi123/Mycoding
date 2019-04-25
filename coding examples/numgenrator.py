def numgenrator(n):
    for i in range(1,n+1):
        if i%5==0 and i%7!=0:
            yield i

n=int(input("enter ypou nu:"))
val=[]
for i in numgenrator(n):
    val.append(str(i))
print ",".join(val)
