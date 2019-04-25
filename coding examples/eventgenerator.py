def evenGenrator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1

n=int(input("enter yur num"))
values=[]
for i in evenGenrator(n):
    values.append(str(i))
print ",".join(values)
