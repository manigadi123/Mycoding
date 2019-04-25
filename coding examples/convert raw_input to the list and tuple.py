#important example:
# The raw input is 32,45,66,55,43,55,78
#the output shpould be in the [32,45,66,55,43,55,78],(32,45,66,55,43,55,78)

v=raw_input("enter the values:")
l=v.split(",")

t=tuple(l)

print t
print l
