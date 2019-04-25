values=raw_input("enter the values of list:")
num=[x for x in values.split(",") if int(x)%2!=0]
print type(num)
b=str(num)
print b
print ",".join(num)

