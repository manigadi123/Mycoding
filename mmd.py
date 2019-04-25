def foo(x, y):
    ab=str(x)*y
    return reduce(lambda i, j: int(i)* int(j) , ab)
print(foo(4,4))
