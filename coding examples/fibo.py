def f(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)

n=raw_input("enter you r value")
print f(n)