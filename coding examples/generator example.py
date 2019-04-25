def gen(x,y=0,z=1):
    if y==0:
        x,y=y,x
        while x<y:
            yield x
            x+=z
b=gen(10)
next(b)
#gen(10,20)
#gen(10,20,2)
