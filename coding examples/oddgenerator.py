def oddgenrator(n):
    i=0
    while i<=n:
        if i%2!=0:
            yield i
        i+=1

n=int(input("enter you nu"))
val=[]
for i in oddgenrator(n):
    val.append(str(i))
print ",".join(val)
