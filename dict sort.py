Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = Dict.keys()
Students.sort()
for S in Students:
      print":".join((S,str(Dict[S])))
#print(dir(Dict))

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print "Length : %d" % len (Dict)


