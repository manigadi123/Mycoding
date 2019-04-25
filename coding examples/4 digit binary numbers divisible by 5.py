values=raw_input("enter the values")
i=[x for x in raw_input().split(',')]
for p in i:
    intp=int(p, 2)
    if not intp%5:
        values.append(p)

print ','.join(values)
